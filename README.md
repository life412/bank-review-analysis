Overview

This project collects, cleans, and analyzes user reviews for three Ethiopian banks’ mobile applications from the Google Play Store.
The goal is to understand customer sentiment, identify key drivers and pain points, and provide actionable insights for app improvement.

Banks Analyzed:

Commercial Bank of Ethiopia (CBE)

Bank of Abyssinia (BOA)

Abyssinia Bank

Project Structure
bank-review-analysis/
│
├── data/               # Folder to store CSV files
│   ├── raw_reviews.csv # Raw scraped reviews
│   └── clean_reviews.csv # Cleaned/preprocessed reviews
│
├── scripts/            # Python scripts
│   ├── scrape_reviews.py      # Scrapes reviews from Google Play
│   ├── preprocess_reviews.py  # Cleans and normalizes raw reviews
│   └── .gitkeep        # Keeps folder tracked in Git
│
├── notebooks/          # Optional notebooks for exploration
│   └── .gitkeep
│
├── requirements.txt    # Python dependencies
└── README.md

Setup

Clone the repository

git clone https://github.com/life412/bank-review-analysis.git
cd bank-review-analysis


Install dependencies

pip install -r requirements.txt

Task 1 — Data Collection & Preprocessing
Scraping Reviews

Collect reviews, ratings, dates, and app names from Google Play using google-play-scraper.

Target: 400+ reviews per bank (1,200+ total).

Example fields: review, rating, date, bank, source.

Script: scripts/scrape_reviews.py

Preprocessing

Remove duplicates and empty reviews.

Normalize dates to YYYY-MM-DD.

Save cleaned data to CSV: data/clean_reviews.csv.

Script: scripts/preprocess_reviews.py

Branching and Version Control

task-1 branch: contains Task 1 scripts and initial data.

main branch: stable version of the project.

Commit frequently with meaningful messages, e.g.,

Add initial scraping script for all three banks

Add preprocessing script and clean CSV

Next Steps

Task 2: Sentiment and thematic analysis

Task 3: Store cleaned data in PostgreSQL

Task 4: Generate insights, visualizations, and recommendations

Dependencies

google-play-scraper

pandas

numpy

nltk

scikit-learn (optional for keyword extraction)

spacy (optional for keyword extraction)
