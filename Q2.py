def stock_portfolio_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2750,
        "MSFT": 310,
        "AMZN": 145
    }

    portfolio = {}
    print("📈 Welcome to the Stock Portfolio Tracker")
    print("Available stocks:", ', '.join(stock_prices.keys()))
    print("Type 'done' to finish input.\n")

    while True:
        stock = input("Enter stock symbol: ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Invalid stock symbol. Please choose from available list.")
            continue
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            if qty < 0:
                print("Quantity cannot be negative.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print("Enter a valid number for quantity.")
            continue

    total_value = 0
    print("\n📊 Portfolio Summary:")
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total_value += value
        print(f"{stock} x {qty} @ ${stock_prices[stock]} = ${value}")

    print(f"\n💰 Total Investment Value: ${total_value}")

    save = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save == "yes":
        filename = "portfolio_summary.txt"
        with open(filename, 'w') as f:
            for stock, qty in portfolio.items():
                value = qty * stock_prices[stock]
                f.write(f"{stock} x {qty} @ ${stock_prices[stock]} = ${value}\n")
            f.write(f"\nTotal Investment: ${total_value}")
        print(f"📄 Summary saved to {filename}")
stock_portfolio_tracker()