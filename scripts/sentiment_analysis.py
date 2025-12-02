# Sentiment Analysis and Theme Extraction for Bank Reviews

import pandas as pd
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load cleaned reviews
df = pd.read_csv("data/clean_reviews.csv")

# -------------------------------
# Step 1: Preprocessing (simple)
# -------------------------------
def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower().strip()
    return text

df["clean_review"] = df["review"].apply(preprocess_text)

# -------------------------------
# Step 2: Sentiment Analysis
# -------------------------------
# Using HuggingFace DistilBERT SST-2
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Apply sentiment
df["sentiment"] = df["clean_review"].apply(lambda x: sentiment_pipeline(x)[0]["label"])
df["sentiment_score"] = df["clean_review"].apply(lambda x: sentiment_pipeline(x)[0]["score"])

# -------------------------------
# Step 3: Keyword Extraction (TF-IDF)
# -------------------------------
vectorizer = TfidfVectorizer(max_features=50, ngram_range=(1,2), stop_words="english")
X = vectorizer.fit_transform(df["clean_review"])

keywords = vectorizer.get_feature_names_out()
print("Top keywords / n-grams:", keywords[:10])

# -------------------------------
# Step 4: Theme Clustering (KMeans)
# -------------------------------
num_themes = 3  # 3 themes per bank as example
kmeans = KMeans(n_clusters=num_themes, random_state=42)
df["theme"] = kmeans.fit_predict(X)

# -------------------------------
# Step 5: Save enriched CSV
# -------------------------------
df.to_csv("data/enriched_reviews.csv", index=False)
print("Enriched reviews saved with sentiment and themes!")
