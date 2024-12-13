# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:49:45 2024

@author: ashwe
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Define the ticker symbol for Infosys on NSE
ticker_symbol = "INFY.NS"

# Calculate the start and end dates
end_date = datetime.today()
start_date = end_date - timedelta(days=10 * 30)  # Approximate 10 months as 300 days

# Fetch historical data using yfinance
def fetch_historical_data(ticker, start, end):
    try:
        ticker_data = yf.Ticker(ticker)
        historical_data = ticker_data.history(start=start, end=end)
        return historical_data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Get the historical data
historical_data = fetch_historical_data(ticker_symbol, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))

if historical_data is not None:
    # Save data to a CSV file
    csv_file = "INFY_last_10_months.csv"
    historical_data.to_csv(csv_file)
    print(f"Data saved to {csv_file}")
else:
    print("Failed to fetch historical data.")

from datetime import datetime

# Define the ticker symbol for Infosys on NSE
ticker_symbol = "INFY.NS"

# Function to fetch intraday data for a specific date
def fetch_intraday_data(ticker, date):
    try:
        ticker_data = yf.Ticker(ticker)
        # Fetch data for the range covering the specific date
        start_date = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
        intraday_data = ticker_data.history(interval="1m", start=start_date, end=date)
        return intraday_data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Specify the date for intraday data
specific_date = "2024-12-12"  # Example date in YYYY-MM-DD format
specific_date1 = "2024-12-13"  # Example date in YYYY-MM-DD format

# Fetch the intraday data
intraday_data = fetch_intraday_data(ticker_symbol, specific_date)

if intraday_data is not None and not intraday_data.empty:
    # Save data to a CSV file
    csv_file = f"INFY_intraday_{specific_date}.csv"
    intraday_data.to_csv(csv_file)
    print(f"Intraday data for {specific_date} saved to {csv_file}")
else:
    print(f"No intraday data available for {specific_date}.")

# Function to fetch the current price of a stock
def fetch_current_price(ticker):
    try:
        ticker_data = yf.Ticker(ticker)
        current_price = ticker_data.info["currentPrice"]
        return current_price
    except Exception as e:
        print(f"Error fetching current price: {e}")
        return None

# Fetch and display the current price of the stock
current_price = fetch_current_price(ticker_symbol)
if current_price is not None:
    print(f"Current price of {ticker_symbol}: {current_price}")