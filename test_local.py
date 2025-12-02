"""
Local test script for Google Maps scraper
Run this to test without Apify
"""
import asyncio
import json
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from playwright.async_api import async_playwright
from scraper import GoogleMapsScraper


async def test_scraper():
    """Test the scraper locally"""
    
    # Test input
    test_input = {
        "searchQuery": "coffee shops",
        "location": "San Francisco, CA",
        "maxResults": 20,
        "deepScrape": False
    }
    
    print("="*60)
    print("🧪 Testing Google Maps Scraper")
    print("="*60)
    print(f"Query: {test_input['searchQuery']}")
    print(f"Location: {test_input['location']}")
    print(f"Max Results: {test_input['maxResults']}")
    print("="*60)
    
    async with async_playwright() as playwright:
        # Launch browser (headless=False to watch it work)
        browser = await playwright.chromium.launch(
            headless=True,  # Set to False to see the browser
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
            ]
        )
        
        try:
            scraper = GoogleMapsScraper(browser)
            
            businesses = await scraper.scrape(
                query=test_input['searchQuery'],
                location=test_input['location'],
                max_results=test_input['maxResults'],
                deep_scrape=test_input['deepScrape']
            )
            
            print(f"\n✅ Successfully scraped {len(businesses)} businesses!\n")
            
            # Display first 3 results
            for i, business in enumerate(businesses[:3], 1):
                print(f"\n{i}. {business.get('title', 'N/A')}")
                print(f"   Category: {business.get('category', 'N/A')}")
                print(f"   Rating: {business.get('rating', 'N/A')} ({business.get('reviewsCount', 0)} reviews)")
                print(f"   Address: {business.get('address', 'N/A')}")
                print(f"   Phone: {business.get('phone', 'N/A')}")
                print(f"   Website: {business.get('website', 'N/A')}")
            
            if len(businesses) > 3:
                print(f"\n... and {len(businesses) - 3} more businesses")
            
            # Save to file
            output_file = 'test_output.json'
            with open(output_file, 'w') as f:
                json.dump(businesses, f, indent=2)
            
            print(f"\n💾 Full results saved to: {output_file}")
            print("\n" + "="*60)
            print("✨ Test completed successfully!")
            print("="*60)
            
        except Exception as e:
            print(f"\n❌ Error during test: {e}")
            import traceback
            traceback.print_exc()
        
        finally:
            await browser.close()


if __name__ == '__main__':
    print("\n🚀 Starting local test...\n")
    asyncio.run(test_scraper())
