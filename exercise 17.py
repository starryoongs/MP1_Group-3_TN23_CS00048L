m = float(input("Input mass of the water: "))
temperature_change = float(input("Input temperature change: "))

c = 4.186

q = m * c * temperature_change

kwh = q / 3_600_00
cost = kwh * 0.089

print("")
print("Energy required: ", q)
print("Cost of heating: ", round(cost, 2))