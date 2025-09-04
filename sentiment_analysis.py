# sentiment_analysis.py
from transformers import pipeline
import pandas as pd
from sqlalchemy import create_engine

# DB setup
engine = create_engine("postgresql://user:password@localhost:5432/stocks")

# Load mock tweets/news
data = {
    "ticker": ["AAPL", "AAPL", "AAPL"],
    "date": ["2024-01-10", "2024-01-11", "2024-01-12"],
    "text": [
        "Apple stock is soaring after new iPhone release!",
        "Investors are worried about Apple's China sales.",
        "Apple beats earnings expectations this quarter."
    ]
}
df = pd.DataFrame(data)

# FinBERT sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="ProsusAI/finbert")

df["sentiment"] = df["text"].apply(lambda x: sentiment_pipeline(x)[0]["label"])
df["sentiment_score"] = df["text"].apply(lambda x: sentiment_pipeline(x)[0]["score"])

# Save to SQL
df.to_sql("sentiment", engine, if_exists="append", index=False)
print("Sentiment stored in SQL!")
