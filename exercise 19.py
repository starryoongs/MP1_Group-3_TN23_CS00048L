import math

height = float(input("Enter height (meters): "))

a = 9.8  

vf = math.sqrt(2 * a * height)

print("Final velocity when hitting the ground is:", vf, "m/s")