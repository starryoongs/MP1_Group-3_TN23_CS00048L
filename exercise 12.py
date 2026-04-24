import math
t1 = float(input("Enter latitude of point 1 (in degrees): "))
g1 = float(input("Enter longitude of point 1 (in degrees): "))
t2 = float(input("Enter latitude of point 2 (in degrees): "))
g2 = float(input("Enter longitude of point 2 (in degrees): "))

t1 = math.radians(t1)
g1 = math.radians(g1)
t2 = math.radians(t2)
g2 = math.radians(g2)

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print(f"\nDistance between the two points is: {distance:.2f} km")