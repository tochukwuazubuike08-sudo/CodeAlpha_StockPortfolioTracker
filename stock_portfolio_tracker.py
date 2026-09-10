from datetime import datetime

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420
}
session_total = 0
stock_list_items = []                          # ← REPLACES the old stock_list line
for stock_name in stock_prices:
    stock_list_items.append(stock_name + " ($" + str(stock_prices[stock_name]) + ")")

stock_list = ", ".join(stock_list_items)

with open("portfolio_results.txt", "a") as file:
    while True:
        stock = input("Enter your preferred stock: " + "\n" + stock_list + ": ").upper()

        if stock in stock_prices:
            price = stock_prices[stock]
            try:
                quantity = int(input("Enter the quantity to check: "))
            except ValueError:
                print("please enter a valid number.")
                continue

            total = quantity * price
            session_total = session_total + total
            print("Total investment value: $", total)
            file.write(
            str(datetime.now()) + " - Stock: " + stock + ", Quantity: " + str(quantity) + ", Price: $" + str(price) + ", Total: $" + str(
                total) + "\n")

        else:
            print("Sorry, stock not available")
            file.write(str(datetime.now()) + " - Stock not available: " + stock + "\n")

        while True:
            choice = input("Do you want to check another stock? (yes/no): ").lower()

            if choice == "yes":
                break
            elif choice == "no":
                break
            else:
                print("Please enter yes or no")
        if choice == "no":
            break

    print("Total invested this session: $" + str(session_total))
    file.write(str(datetime.now()) + " - SESSION SUMMARY: Total invested this session: $" + str(session_total) + "\n")

