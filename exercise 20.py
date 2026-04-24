pressure = float(input("Put the pressure number: "))
volume = float(input("Put the volume number: "))
temperature = float(input("Put the temperature: "))

k = input("C/F: ")
r = 8.314

if k == "C":
    temp_kelvin = temperature + 273.15
else:5
temp_kelvin = (temperature - 32) * 5/9 + 273.15
   
n = (pressure * volume) / (r * temp_kelvin)

print("Your gas is: ", n)