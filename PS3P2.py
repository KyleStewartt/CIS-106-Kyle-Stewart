purchasePricePerShare = float(input("Enter the purchase price per share: "))
currentStockPrice = float(input("Enter the current stock price: "))
quantityOfStock = int(input("Enter the quantity of stock: "))
valueOfStock = (currentStockPrice - purchasePricePerShare) * quantityOfStock
print("The value of the stock has changed by:", valueOfStock)