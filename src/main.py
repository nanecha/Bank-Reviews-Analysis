
from scraper import fetch_reviews
if __name__ == "__main__":
    target_banks = ["com.bank1.app", "com.bank2.app"]
    reviews = fetch_reviews(target_banks)
    print(f"Final review count: {len(reviews)}")