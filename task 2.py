import yfinance as yf

portfolio = {}
total_value = 0

print("📈 Real-Time Stock Portfolio Tracker (Yahoo Finance)")
print("Enter 'done' when finished.\n")

while True:
    stock = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
    if stock == "DONE":
        break
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        if qty < 0:
            print("⚠️ Quantity must be positive.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("⚠️ Please enter a valid number.")

print("\n🔄 Fetching live prices...\n")

print("📊 Your Live Portfolio Summary:")
for stock, qty in portfolio.items():
    ticker = yf.Ticker(stock)
    price = ticker.info['regularMarketPrice']
    value = qty * price
    total_value += value
    print(f"{stock}: {qty} × ₹{price:.2f} = ₹{value:.2f}")

print(f"\n💰 Total Live Investment: ₹{total_value:.2f}")
