import requests
import pandas as pd
import datetime
today = datetime.date.today()
today_str=str(today)

# Function to get top 500 US stocks from Wikipedia
def get_top_500_stocks():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(url)
    table = pd.read_html(response.text)
    df = table[0]
    return df['Symbol'].tolist()[:500]

# Function to download daily closing prices
def download_prices(ticker, start_date, end_date):
    url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={start_date}&period2={end_date}&interval=1d&events=history"
    response = requests.get(url)
    data = pd.read_csv(url)
    return data

# Main function to run the script
def main(start_date, end_date):
    # Get top 500 US stocks
    tickers = get_top_500_stocks()
    
    # Define start and end date
    start_date_unix = int(pd.to_datetime(start_date).timestamp())
    end_date_unix = int(pd.to_datetime(end_date).timestamp())
    
    # Create an empty DataFrame to store the data
    df_final = pd.DataFrame(columns=['Ticker', 'Date', 'Price'])

    for ticker in tickers:
        try:
            # Download daily closing prices
            data = download_prices(ticker, start_date_unix, end_date_unix)
            data['Ticker'] = ticker
            data.rename(columns={'Date': 'Date', 'Adj Close': 'Price'}, inplace=True)
            data = data[['Ticker', 'Date', 'Price']]
            
            # Concatenate data to the final DataFrame
            df_final = pd.concat([df_final, data], ignore_index=True)
        except Exception as e:
            print(f"Failed to download data for {ticker}: {str(e)}")
    
    # Save data to CSV
    df_final.to_csv('top_500_us_stocks_now.csv', index=False)

if __name__ == "__main__":
    #start_date = input("Enter the start date (YYYY-MM-DD): ")
    #end_date = input("Enter the end date (YYYY-MM-DD): ")
    start_date="2023-01-01"
    end_date=str(today)
    main(start_date, end_date)
