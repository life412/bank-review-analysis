from transformers import pipeline
import pandas as pd

df = pd.read_csv("data/clean_reviews.csv")

classifier = pipeline("sentiment-analysis")

sentiments = classifier(df["review"].tolist())

df["sentiment"] = [s["label"] for s in sentiments]
df.to_csv("data/clean_reviews.csv", index=False)

print("Sentiment added!")
