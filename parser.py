"""
Parser module for extracting business data from Google Maps
"""
from typing import Optional, Dict, Any
from playwright.async_api import Page, ElementHandle
import logging
from utils import (
    extract_rating, extract_reviews_count, extract_phone,
    extract_coordinates_from_url, extract_place_id, normalize_address,
    parse_hours
)
from config import SELECTORS

logger = logging.getLogger(__name__)


class GoogleMapsParser:
    """Parser for Google Maps business data"""
    
    def __init__(self, page: Page):
        self.page = page
    
    async def parse_business_card(self, card: ElementHandle) -> Optional[Dict[str, Any]]:
        """
        Parse basic information from a business card in search results
        
        Args:
            card: ElementHandle of the business card
            
        Returns:
            Dictionary with business data or None if parsing fails
        """
        try:
            data = {}
            
            # Get the link element which contains most basic info
            link = await card.query_selector('a')
            if not link:
                return None
            
            # Business name
            name_elem = await link.query_selector('[class*="fontHeadlineSmall"]')
            if name_elem:
                data['title'] = await name_elem.inner_text()
            else:
                return None  # Skip if no name
            
            # Rating
            rating_elem = await card.query_selector('span[role="img"]')
            if rating_elem:
                aria_label = await rating_elem.get_attribute('aria-label')
                data['rating'] = extract_rating(aria_label)
            
            # Reviews count
            reviews_elem = await card.query_selector('span[aria-label*="review"]')
            if reviews_elem:
                reviews_text = await reviews_elem.inner_text()
                data['reviewsCount'] = extract_reviews_count(reviews_text)
            
            # Category
            category_elem = await card.query_selector('[class*="fontBodyMedium"] > span')
            if category_elem:
                category_text = await category_elem.inner_text()
                # Category is usually like "Coffee shop · $$ · Open now"
                parts = category_text.split('·')
                if parts:
                    data['category'] = parts[0].strip()
                
                # Price level
                for part in parts:
                    part = part.strip()
                    if '$' in part:
                        data['priceLevel'] = part
            
            # Get URL for place ID
            href = await link.get_attribute('href')
            if href:
                data['url'] = f"https://www.google.com{href}" if href.startswith('/') else href
                data['placeId'] = extract_place_id(data['url'])
                
                # Try to get coordinates from URL
                coords = extract_coordinates_from_url(data['url'])
                if coords:
                    data['coordinates'] = coords
            
            return data
            
        except Exception as e:
            logger.error(f"Error parsing business card: {e}")
            return None
    
    async def parse_business_details(self, deep_scrape: bool = False) -> Dict[str, Any]:
        """
        Parse detailed information from business detail page
        
        Args:
            deep_scrape: If True, extract additional details like reviews
            
        Returns:
            Dictionary with detailed business data
        """
        data = {}
        
        try:
            # Wait for content to load
            await self.page.wait_for_selector('h1', timeout=5000)
            
            # Business name
            name = await self.page.query_selector('h1')
            if name:
                data['title'] = await name.inner_text()
            
            # Rating and reviews
            rating_elem = await self.page.query_selector('span[role="img"][aria-label*="star"]')
            if rating_elem:
                aria_label = await rating_elem.get_attribute('aria-label')
                data['rating'] = extract_rating(aria_label)
            
            reviews_elem = await self.page.query_selector('button[aria-label*="review"]')
            if reviews_elem:
                reviews_text = await reviews_elem.inner_text()
                data['reviewsCount'] = extract_reviews_count(reviews_text)
            
            # Address
            address_button = await self.page.query_selector('button[data-item-id*="address"]')
            if address_button:
                address_text = await address_button.inner_text()
                data['address'] = normalize_address(address_text)
            
            # Phone
            phone_button = await self.page.query_selector('button[data-item-id*="phone"]')
            if phone_button:
                phone_text = await phone_button.inner_text()
                data['phone'] = extract_phone(phone_text)
            
            # Website
            website_link = await self.page.query_selector('a[data-item-id*="authority"]')
            if website_link:
                data['website'] = await website_link.get_attribute('href')
            
            # Category/Type
            category_button = await self.page.query_selector('button[jsaction*="category"]')
            if category_button:
                data['category'] = await category_button.inner_text()
            
            # Hours
            hours_button = await self.page.query_selector('button[aria-label*="Hours"]')
            if hours_button:
                # Click to expand hours
                await hours_button.click()
                await self.page.wait_for_timeout(500)
                
                hours_container = await self.page.query_selector('div[aria-label*="Hours"]')
                if hours_container:
                    hours_text = await hours_container.inner_text()
                    data['hours'] = parse_hours(hours_text)
            
            # Plus Code
            plus_code = await self.page.query_selector('button[data-item-id*="oloc"]')
            if plus_code:
                data['plusCode'] = await plus_code.inner_text()
            
            # Get current URL for place ID and coordinates
            current_url = self.page.url
            data['url'] = current_url
            data['placeId'] = extract_place_id(current_url)
            
            coords = extract_coordinates_from_url(current_url)
            if coords:
                data['coordinates'] = coords
            
            # Deep scrape: reviews
            if deep_scrape:
                # This would require additional clicking and parsing
                # Placeholder for now
                data['reviews'] = []
            
            return data
            
        except Exception as e:
            logger.error(f"Error parsing business details: {e}")
            return data
    
    async def has_captcha(self) -> bool:
        """Check if CAPTCHA is present"""
        try:
            captcha = await self.page.query_selector('iframe[src*="recaptcha"]')
            return captcha is not None
        except:
            return False
    
    async def has_no_results(self) -> bool:
        """Check if search returned no results"""
        try:
            no_results = await self.page.query_selector('text="No results found"')
            return no_results is not None
        except:
            return False
