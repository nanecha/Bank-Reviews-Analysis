import time
from typing import List, Dict, Any
from google_play_scraper import reviews_all


def fetch_reviews(banks: List[str], max_reviews_per_bank: int = 400) -> List[Dict[str, Any]]:
    """
    Fetches app reviews for a list of bank apps from the Google Play Store.
    Args:
        banks: List of app IDs (package names) to scrape.
        max_reviews_per_bank: Maximum number of reviews to fetch per app.     
    Returns:
        List of review dictionaries.
    """
    all_reviews: List[Dict[str, Any]] = []

    for bank in banks:
        try:
            print(f"Fetching reviews for bank: {bank}")

            reviews = reviews_all(
                app_id=bank,
                sleep_milliseconds=0,  # Consider adding a small delay to avoid rate-limiting
                lang='en',
                country='us'
            )

            # Limit the number of reviews and add to collection
            all_reviews.extend(reviews[:max_reviews_per_bank])
            print(
                f"Successfully fetched {len(reviews[:max_reviews_per_bank])} reviews for {bank}")

        except Exception as e:
            print(f"Error fetching reviews for {bank}: {str(e)}")
            continue  # Continue with next bank instead of returning

        # Progress update
        print(f"Total reviews fetched so far: {len(all_reviews)}")

    return all_reviews
