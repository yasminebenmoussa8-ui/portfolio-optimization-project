import yfinance as yf
from datetime import datetime, timedelta

def fetch_stock_prices(tickers):
    """
    Dynamically calculates a 3-year lookback window and downloads 
    historical closing prices from Yahoo Finance.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    three_years_ago = (datetime.now() - timedelta(days=3*365)).strftime("%Y-%m-%d")
    print(f"Downloading historical data from {three_years_ago} to {today}...")
    
    # Download close prices using your exact configuration
    stock_prices_df = yf.download(tickers, start=three_years_ago, end=today)['Close']
    return stock_prices_df