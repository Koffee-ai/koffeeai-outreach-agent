# scraper.py

import random

# Dummy scraper for testing
def scrape_businesses(category, location, max_contacts):
    sample_businesses = [
        {
            "name": f"{category.title()} Business {i+1}",
            "email": f"{category}{i+1}@example.com",
            "phone": f"+91 90000{i:04d}",
            "socials": {
                "instagram": f"https://instagram.com/{category}{i+1}",
                "facebook": f"https://facebook.com/{category}{i+1}",
                "linkedin": f"https://linkedin.com/in/{category}{i+1}",
            }
        }
        for i in range(max_contacts)
    ]
    # Simulate scraping delay
    print(f"[SCRAPER] Fetched {len(sample_businesses)} businesses in {location}")
    return sample_businesses
