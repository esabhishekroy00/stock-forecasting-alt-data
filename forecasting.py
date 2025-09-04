from prophet import Prophet
import pandas as pd
from sqlalchemy import create_engine


def forecast_stock(ticker="AAPL", periods=30, db_url="postgresql://user:password@localhost:5432/stocks"):
    """
    Generate a stock price forecast using Prophet and save results to CSV.

    Args:
        ticker (str): Stock ticker symbol (default: "AAPL")
        periods (int): Number of days into the future to forecast
        db_url (str): SQLAlchemy database connection string
    """
    # Connect to database
    engine = create_engine(db_url)

    # Load historical stock data
    query = f"SELECT date, close FROM stocks WHERE ticker='{ticker}';"
    df = pd.read_sql(query, engine)

    # Prophet requires 'ds' (date) and 'y' (value)
    df.rename(columns={"date": "ds", "close": "y"}, inplace=True)

    # Fit Prophet model
    model = Prophet()
    model.fit(df)

    # Create future dataframe
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    # Save forecast to CSV
    output_file = f"{ticker.lower()}_forecast.csv"
    forecast.to_csv(output_file, index=False)

    print(f"✅ Forecast for {ticker} saved to {output_file}")


if __name__ == "__main__":
    forecast_stock()
