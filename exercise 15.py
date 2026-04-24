feet = float(input("Enter a measurement in feet: "))

inches = feet * 12
yards = feet / 3
miles = feet / 5280

print("\nMeasurement Conversions:")
print(f"In inches: {inches:.2f}")
print(f"In yards: {yards:.2f}")
print(f"In miles: {miles:.4f}")
