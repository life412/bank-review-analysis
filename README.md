# Bank Review Analytics

This project analyzes customer reviews from major Ethiopian banking apps to extract insights, sentiment, and common issues.

## Features
- Scrapes Google Play Store reviews
- Cleans and preprocesses text
- Sentiment analysis using DistilBERT
- Thematic extraction
- PostgreSQL database integration
- Visual analysis with Jupyter Notebook

## Folder Structure
scripts/
data/
notebooks/

markdown
Copy code

## How to Run
1. Install requirements:
pip install google-play-scraper pandas transformers torch

markdown
Copy code

2. Run scraping:
python scripts/scrape_reviews.py

markdown
Copy code

3. Preprocess:
python scripts/preprocess_reviews.py

markdown
Copy code

4. Sentiment:
python scripts/sentiment_analysis.py

Copy code
