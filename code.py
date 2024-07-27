import requests

# Replace with your Alpha Vantage API key
API_KEY = 'YOUR_API_KEY_HERE'
USD_TO_INR_RATE = 75  # Exchange rate from USD to INR

# Function to fetch real-time stock data
def get_stock_price_in_inr(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url).json()
    if 'Global Quote' in response:
        price_usd = float(response['Global Quote']['05. price'])
        return price_usd * USD_TO_INR_RATE
    else:
        print(f"Failed to fetch data for {symbol}: {response}")
        return None

# Function to add a stock to the portfolio
def add_stock(portfolio, symbol, shares):
    price_inr = get_stock_price_in_inr(symbol)
    if price_inr is not None:
        portfolio[symbol] = {'shares': shares, 'price': price_inr}
        print(f"{symbol} added to portfolio with price ₹{price_inr:.2f}.")

# Function to remove a stock from the portfolio
def remove_stock(portfolio, symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from portfolio.")
    else:
        print(f"{symbol} not found in portfolio.")

# Function to calculate the total portfolio value
def calculate_portfolio_value(portfolio):
    total_value = 0.0
    for symbol, data in portfolio.items():
        current_price_inr = get_stock_price_in_inr(symbol)
        if current_price_inr is not None:
            total_value += current_price_inr * data['shares']
            print(f"Current price of {symbol} in INR: ₹{current_price_inr:.2f}")
    return total_value

# Example usage
if __name__ == "__main__":
    portfolio = {}

    # Adding stocks to the portfolio
    add_stock(portfolio, 'GOOGL', 5)
    add_stock(portfolio, 'RELIANCE.BSE', 10)

    # Displaying current portfolio
    print("\nCurrent Portfolio:")
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['shares']} shares at ₹{data['price']:.2f} each")

    # Calculating total portfolio value
    total_value = calculate_portfolio_value(portfolio)
    print(f"\nTotal Portfolio Value: ₹{total_value:.2f}")

    # Removing a stock from the portfolio
    remove_stock(portfolio, 'GOOGL')

    # Displaying updated portfolio
    print("\nUpdated Portfolio:")
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['shares']} shares at ₹{data['price']:.2f} each")

    # Calculating total portfolio value again
    total_value = calculate_portfolio_value(portfolio)
    print(f"\nTotal Portfolio Value: ₹{total_value:.2f}")
