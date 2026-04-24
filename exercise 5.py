small = int (input("Enter number of containers (1 liter or less): "))
large = int (input("Enter number of containers (more than 1 liter): "))
refund = small * 0.10 + large * 0.25
print ("Refund will be: $%.2f" % refund)