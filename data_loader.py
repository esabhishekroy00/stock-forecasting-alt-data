# data_loader.py
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

# DB setup
engine = create_engine("postgresql://user:password@localhost:5432/stocks")

# Download stock data
ticker = "AAPL"
df = yf.download(ticker, start="2020-01-01", end="2024-01-01")
df.reset_index(inplace=True)
df["ticker"] = ticker

# Push to SQL
df.to_sql("stocks", engine, if_exists="append", index=False)
print("Data loaded to SQL!")
