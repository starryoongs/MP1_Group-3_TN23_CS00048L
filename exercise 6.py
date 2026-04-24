meal = float(input("Enter the cost of the meal: "))

tax_rate = 0.12
tax = meal * tax_rate
tip = meal * 0.18
total = meal + tax + tip

print("Tax: $%.2f" % tax)
print("Tip: $%.2f" % tip)
print("Total: $%.2f" % total)