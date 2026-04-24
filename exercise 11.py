mpg = float(input("Input fuel efficiency in MPG:"))
Formula = 235.215/mpg

print(f"\nFuel Efficiency in American units: {mpg:.2f} mpg")
print("Formula = 235.215 / 1 US mpg")
print(f"The equivalent Fuel Efficiency in Canadian units: {Formula:.2f} L/100km")