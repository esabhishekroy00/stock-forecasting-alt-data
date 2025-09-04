# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Stock Market Forecasting with Sentiment")

# Load forecast
df = pd.read_csv("aapl_forecast.csv")

fig = px.line(df, x="ds", y=["yhat", "yhat_lower", "yhat_upper"], 
              title="AAPL Stock Forecast")
st.plotly_chart(fig)

st.subheader("Latest Sentiment")
sentiment_df = pd.read_csv("sentiment_sample.csv")  # or pull from SQL
st.write(sentiment_df)
