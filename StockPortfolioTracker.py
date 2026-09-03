portfolio={}
cash = float(input("Enter your available cash: ₹"))
def buy_stock():
    global cash
    symbol=input("Enter a symbol:").upper()
    quantity=int(input("Enter quantity:"))
    price=float(input("Enter a price:"))
    cost=quantity*price
    if cost > cash:
        print("Doesn't have enough cash available")
        return
    if symbol in portfolio:
        stock = portfolio[symbol]
        old_quantity=stock["quantity"]
        old_investment=old_quantity*stock["avg_price"]
        new_quantity=old_quantity+quantity
        new_investment=old_investment+cost
        stock["quantity"]=old_quantity+quantity
        stock["avg_price"]=new_investment/new_quantity
    else:
        portfolio[symbol]={
            "quantity":quantity,
            "avg_price":price,
            "current_price":price
        }
    cash-=cost
    print("Stock bought successfully!\n")
def sell_stock():
    global cash
    symbol=input("Enter stock symbol:").upper()
    if symbol not in portfolio:
        print("Stock not found")
        return
    quantity = int(input("Enter quantity to sell:"))
    stock=portfolio[symbol]
    if quantity > stock["quantity"]:
        print("You don't own enough shares")
        return
    price=float(input("Enter selling price:"))
    cash+=(quantity*price)
    stock["quantity"]-=quantity
    if stock["quantity"]==0:
        del portfolio[symbol]
    print("Stock sold successfully!")
def update_price():
    symbol=input("Enter stock symbol: ").upper()
    if symbol not in portfolio:
        print("Symbol not found")
        return
    price=float(input("Enter current market price:"))
    portfolio[symbol]["current_price"]=price
    print("Price updated")
def view_portfolio():
    if not portfolio:
        print("Portfolio is empty")
        return
    total_investment=0
    total_value=0
    print("\n======= Portfolio =======")
    for symbol,stock in portfolio.items():
        quantity=stock["quantity"]
        avg_price=stock["avg_price"]
        current_price=stock["current_price"]
        investment=quantity*avg_price
        value=quantity*current_price
        profit_loss=value-investment
        total_investment+=investment
        total_value+=value
        print(f"\nStock: {symbol}")
        print(f"\nQuantity: {quantity}")
        print(f"\nAverage price: {avg_price:.2f}")
        print(f"\nCurrent price: {current_price:.2f}")
        print(f"\nInvestment: {investment:.2f}")
        print(f"\nCurrent Value: {value:.2f}")
        if profit_loss>=0:
            print(f"Profit: ₹{profit_loss:.2f}")
        else:
            print(f"Loss: ₹{abs(profit_loss):.2f}")
        total_profit_loss=total_value-total_investment
        print("\n-------")
        print(f"Total investment: ₹{total_investment:.2f}")
        print(f"Current value: {total_value:.2f}")
        print(f"Cash balance: ₹{cash:.2f}")
        if total_profit_loss>=0:
            print(f"Total profit: ₹{total_profit_loss:.2f}")
        else:
            print(f"Total loss: {abs(total_profit_loss):.2f}")
def main():
    while True:
        print("\n======= Stock Portfolio Tracker =======")
        print("1.Buy Stock")
        print("2.Sell Stock")
        print("3.Update Market Price")
        print("4.View Details")
        print("5.Exit")
        choice=input("Enter your choice:")
        if choice == '1':
            buy_stock()
        elif choice == '2':
            sell_stock()
        elif choice == '3':
            update_price()
        elif choice == '4':
            view_portfolio()
        else:
            print("Enter a valid choice\n")
if __name__=="__main__":
    main()