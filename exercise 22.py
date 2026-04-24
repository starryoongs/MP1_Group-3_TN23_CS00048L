import math

side_one = int(input("Input Side One: "))
side_two = int(input("Input Side Two "))
side_three = int(input("Input Side Three: "))

s = (side_one + side_two + side_three) / 2
a = math.sqrt(s * (s - side_one) * (s - side_two) * (s - side_three))

print("The area of the triangle is: ", a)