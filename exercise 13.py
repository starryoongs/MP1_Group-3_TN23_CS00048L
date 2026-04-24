cents = int(input("Enter the number of cents: "))

toonies = cents // 200
cents %= 200
loonies = cents // 100
cents %= 100
quarters = cents // 25
cents %= 25
dimes = cents // 10
cents %= 10
nickels = cents // 5
cents %= 5
pennies = cents

print("\nMinimum coins needed:")
print(f"Toonies: {toonies}")
print(f"Loonis: {loonies}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")

