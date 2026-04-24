import math

r = float(input("Input radius of the cylinder: "))
h = float(input("Input height of the cylinder: "))

v = math.pi * (r**2) * h


print("The volume of the cylinder is: ", round(v, 1))