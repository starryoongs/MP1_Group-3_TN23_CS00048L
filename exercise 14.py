feet = float(input("Enter your height in feet: "))
inches = float(input("Enter your height in inches: "))

total_inches = (feet * 12) + inches
centimeters = total_inches * 2.54

print(f"\nHeight in centimeters {centimeters:.2f} cm")