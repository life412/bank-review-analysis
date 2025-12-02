from google_play_scraper import Sort, reviews
import pandas as pd

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "boa.et.mobilebanking",
    "Abyssinia": "com.bankofabyssinia.mobilebanking"
}

all_reviews = []

for bank, app_id in apps.items():
    result, _ = reviews(
        app_id,
        sort=Sort.NEWEST,
        count=500
    )

    for r in result:
        all_reviews.append({
            "review": r["content"],
            "rating": r["score"],
            "date": r["at"],
            "bank": bank
        })

df = pd.DataFrame(all_reviews)
df.to_csv("data/raw_reviews.csv", index=False)

print("Saved raw reviews!")
