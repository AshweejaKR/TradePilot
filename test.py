# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:49:45 2024

@author: ashwe
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import datetime as dt

# Define the ticker symbol for Infosys on NSE
ticker_symbol = "INFY.NS"

# Calculate the start and end dates
end_date = datetime.today()
start_date = end_date - timedelta(days=10 * 30)  # Approximate 10 months as 300 days

# Fetch historical data using yfinance
def fetch_historical_data(ticker, start, end):
    try:
        ticker_data = yf.Ticker(ticker)
        # Ensure date is a string before processing
        # date = date.strftime("%Y-%m-%d")

        historical_data = ticker_data.history(start=start, end=end)
        return historical_data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# Function to fetch intraday data for a specific date
def fetch_intraday_data(ticker, date):
    try:
        ticker_data = yf.Ticker(ticker)
        # Ensure date is a string before processing
        date = date.strftime("%Y-%m-%d")

        # Fetch data for the range covering the specific date
        start_date = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
        intraday_data = ticker_data.history(interval="1m", start=start_date, end=date)
        return intraday_data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# Function to fetch the current price of a stock
def fetch_current_price(ticker):
    try:
        ticker_data = yf.Ticker(ticker)
        current_price = ticker_data.info["currentPrice"]
        return current_price
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

datestamp=dt.date.today()
data = fetch_intraday_data(ticker_symbol, datestamp)
intraday_data = []
max_ = 9
ct = 0
for i in data['Open']:
    intraday_data.append(i)
    ct = ct + 1
    if ct > max_:
        ct = 0
        break

for i in data['High']:
    intraday_data.append(i)
    ct = ct + 1
    if ct > max_:
        ct = 0
        break

for i in data['Low']:
    intraday_data.append(i)
    ct = ct + 1
    if ct > max_:
        ct = 0
        break

for i in data['Close']:
    intraday_data.append(i)
    ct = ct + 1
    if ct > max_:
        ct = 0
        break

for i in intraday_data:
    print(i)
