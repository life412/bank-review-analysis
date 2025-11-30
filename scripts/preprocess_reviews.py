import pandas as pd

df = pd.read_csv("data/raw_reviews.csv")

# Drop duplicates
df.drop_duplicates(subset=["review"], inplace=True)

# Drop rows with empty reviews
df.dropna(subset=["review"], inplace=True)

# Normalize dates
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

df.to_csv("data/clean_reviews.csv", index=False)

print("Saved clean reviews!")
