import psycopg2
import pandas as pd

conn = psycopg2.connect(
    dbname="bank_reviews",
    user="postgres",
    password="yourpassword",
    host="localhost"
)

cur = conn.cursor()

df = pd.read_csv("data/clean_reviews.csv")

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO reviews (bank, review, rating, sentiment, date)
        VALUES (%s, %s, %s, %s, %s)
    """, (row["bank"], row["review"], row["rating"], row["sentiment"], row["date"]))

conn.commit()
cur.close()
conn.close()

print("Inserted into database!")
