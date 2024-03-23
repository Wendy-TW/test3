import yfinance as yf
import pandas as pd
from datetime import datetime

# Function to get top 500 US stocks from Yahoo Finance
def get_top_500_stocks():
    table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    return df['Symbol'].tolist()[:500]

# Function to download daily closing prices
def download_prices(tickers, start_date, end_date):
    data = {}
    for ticker in tickers:
        try:
            stock = yf.download(ticker, start=start_date, end=end_date)
            data[ticker] = stock['Adj Close']
        except:
            print(f"Failed to download data for {ticker}")
    return data

# Main function to run the script
def main():
    # Get top 500 US stocks
    tickers = get_top_500_stocks()
    
    # Define start and end date
    start_date = '2024-01-01'
    end_date = '2024-12-31'
    
    # Download daily closing prices
    data = download_prices(tickers, start_date, end_date)
    
    # Create a DataFrame to store the data
    df = pd.DataFrame(data)
    df.reset_index(inplace=True)
    
    # Melt DataFrame to have ticker, date, and price columns
    df = pd.melt(df, id_vars=['Date'], var_name='Ticker', value_name='Price')
    
    # Save data to CSV
    df.to_csv('top_500_us_stocks_2024.csv', index=False)

if __name__ == "__main__":
    main()

