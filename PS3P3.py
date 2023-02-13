totalForMeal = float(input("Enter the total for the meal: "))
tip1 = totalForMeal * 0.15
tip2 = totalForMeal * 0.18
tip3 = totalForMeal * 0.20
totalWithTip1 = totalForMeal + tip1
totalWithTip2 = totalForMeal + tip2
totalWithTip3 = totalForMeal + tip3
print("With 15% Tip:")
print("Total:              ", totalForMeal)
print("Tip:                  ", tip1)
print("Total with Tip: ", totalWithTip1, "\n")
print("With 18% Tip:")
print("Total:              ", totalForMeal)
print("Tip:                  ", tip2)
print("Total with Tip: ", totalWithTip2, "\n")
print("With 20% Tip:")
print("Total:              ", totalForMeal)
print("Tip:                  ", tip3)
print("Total with Tip: ", totalWithTip3)