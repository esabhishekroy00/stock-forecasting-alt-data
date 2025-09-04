# stock-forecasting-alt-data
# 📈 Stock Market Forecasting with Alternative Data  

## 📌 Overview  
This project predicts stock price movements by combining **historical stock market data** with **sentiment analysis** from financial news, Reddit, and Twitter.  
It integrates **SQL for structured storage**, **Python for ML/NLP**, and a **Streamlit dashboard** for interactive forecasting.  

---

## 🛠️ Tech Stack  
- **SQL (Postgres/MySQL)** → Store historical stock + sentiment data  
- **Python** →  
  - `yfinance` → Stock price data  
  - `prophet` → Time-series forecasting  
  - `transformers (FinBERT)` → Financial sentiment analysis  
  - `pandas`, `plotly`, `seaborn` → Data handling & visualization  
- **Streamlit** → Interactive dashboard  

---

## 📂 Project Structure  
📁 stock-forecasting-alt-data
│── sql_schema.sql # SQL schema for stocks & sentiment
│── data_loader.py # Loads stock data into SQL
│── sentiment_analysis.py # Runs NLP sentiment on tweets/news
│── forecasting.py # Prophet forecast model
│── dashboard.py # Streamlit dashboard
│── requirements.txt
│── README.md



## 🚀 How to Run  
1. Setup Database  
Create PostgreSQL/MySQL DB, then run:  
```bash
psql -U username -d stocksdb -f sql_schema.sql
2. Install Dependencies bash
pip install -r requirements.txt
3. Load Stock Data bash
python data_loader.py
4. Run Sentiment Analysis bash
python sentiment_analysis.py
5. Forecast Stock Prices bash
python forecasting.py
6. Launch Dashboard bash
streamlit run dashboard.py
