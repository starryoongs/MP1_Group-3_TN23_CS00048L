num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
num3 = int(input('Enter number 3: '))

smallest = min([num1, num2, num3])
largest = max([num1, num2, num3])
middle = (num1 + num2 + num3) - (smallest + largest)

print ('The smallest value is: ', smallest)
print ('The largest value is: ', largest)
print ('The middle value is: ', middle)