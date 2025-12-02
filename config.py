"""
Configuration constants for Google Maps scraper
"""

# Google Maps selectors (as of Dec 2025)
SELECTORS = {
    # Search
    'search_input': 'input#searchboxinput',
    'search_button': 'button[aria-label*="Search"]',
    
    # Results
    'results_container': 'div[role="feed"]',
    'business_cards': 'div[role="article"]',
    'loading_indicator': 'div[class*="loading"]',
    
    # Business details
    'business_name': 'h1',
    'rating': 'span[role="img"][aria-label*="star"]',
    'reviews_count': 'button[aria-label*="review"]',
    'address': 'button[data-item-id*="address"]',
    'phone': 'button[data-item-id*="phone"]',
    'website': 'a[data-item-id*="authority"]',
    'category': 'button[jsaction*="category"]',
    'hours': 'div[aria-label*="Hours"]',
    'price_level': 'span[aria-label*="Price"]',
}

# Timing configurations (in seconds)
TIMING = {
    'page_load': 5,
    'search_wait': 3,
    'scroll_delay_min': 1,
    'scroll_delay_max': 3,
    'business_card_delay': 0.5,
    'retry_delay': 2,
    'captcha_wait': 30,
}

# Retry configuration
RETRY_CONFIG = {
    'max_attempts': 3,
    'multiplier': 2,
    'min_wait': 2,
    'max_wait': 10,
}

# Anti-detection settings
ANTI_DETECTION = {
    'viewport': {
        'width': 1920,
        'height': 1080,
    },
    'user_agents': [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    ],
    'languages': ['en-US', 'en'],
}

# Default values
DEFAULTS = {
    'max_results': 100,
    'language': 'en',
    'deep_scrape': False,
    'include_reviews': False,
    'reviews_per_business': 10,
}

# URLs
GOOGLE_MAPS_URL = 'https://www.google.com/maps'
