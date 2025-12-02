import pandas as pd

df = pd.read_csv("data/raw_reviews.csv")

df.drop_duplicates(subset=["review"], inplace=True)
df.dropna(subset=["review"], inplace=True)

df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

df.to_csv("data/clean_reviews.csv", index=False)
print("Saved clean reviews!")
