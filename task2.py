# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 150
}

total_investment = 0

num_stocks = int(input("How many stocks do you own? "))

for i in range(num_stocks):
    stock_name = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"Value of {stock_name}: ${investment}")
    else:
        print("Stock not found in portfolio.")

print("\nTotal Investment Value: $", total_investment)

# Optional: Save result to a text file
save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write(f"Total Investment Value: ${total_investment}")
    print("Result saved to portfolio.txt")
