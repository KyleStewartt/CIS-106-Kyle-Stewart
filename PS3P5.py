fixedCosts = float(input("Enter fixed costs: "))
pricePerUnit = float(input("Enter price per unit: "))
costPerUnit = float(input("Enter cost per unit: "))
breakEvenPoint = fixedCosts / (pricePerUnit - costPerUnit)
print("The break even point is", breakEvenPoint, "units.")