initial = float(input("Enter initial amount:"))
year1 = 1
year2 = 2
year3 = 3
rate = 0.04
x = initial * (1+rate) ** year1
y = initial * (1+rate) ** year2
z = initial * (1+rate) ** year3
print("------------------------------")
print(f"Savings account balance: {initial: .2f}")
print(f"\nAfter 1 year: {x:.2f}")
print(f"After 2 years: {y:.2f}")
print(f"After 3 years: {z:.2f}")
