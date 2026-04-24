import math

sides = float(input("Put the length sides of a polygon: "))
number_of_sides = int(input("Put the number of sides: "))

s = sides
n = number_of_sides

squared_value = s ** 2
numerator = n * squared_value
denominator = math.tan(math.pi / n) * 4
area_of_polygon = numerator / denominator

print("The area of the polygon is: ", area_of_polygon)