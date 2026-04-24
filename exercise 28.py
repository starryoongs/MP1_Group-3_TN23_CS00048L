Ta = float(input('Enter the air temperature(Celsius): '))
V = float(input('Enter the wind speed(KPH): '))

WCI = 13.12 +  (0.6215 * Ta) - (11.37 * (V**0.16)) + (0.3965 * Ta * V**0.16)

print(f"The calculated wind chill index is: {round(WCI)}")