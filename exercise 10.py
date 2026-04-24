import math
a = int(input("Enter first integer:"))
b = int(input("Enter second integer:"))
sum = a + b
difference = b - a
product = a * b
quotient = a / b
remainder = a % b
log = math.log10(a)
power = math.pow(a, b)
print(f"\nsum of {a} + {b} is: {sum}")
print(f"difference of {b} - {a} is: {difference}")
print(f"product of {a} * {b} is: {product}")
print(f"quotient of {a} / {b} is: {quotient:.1f}")
print(f"remainder of {a} % {b} is: {remainder}")
print(f"base-10 logarithm of {a} is: {log: .2f}")
print(f"{a} to the power of {b} is: {power:.2f}")