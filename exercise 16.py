import math

r = float(input("Enter radius: "))
area = math.pi * (r ** 2)
volume = 4/3 * math.pi * (r ** 3)

print("\nCalculations")
print(f"Area of a circle: {area:.2f}")
print(f"Volume of a sphere: {volume:.2f}")