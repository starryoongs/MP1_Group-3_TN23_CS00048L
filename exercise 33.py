bread = int(input('How many bread will you buy: '))
dayOldBread = int(input('How many day old bread will you buy: '))

breadPrice = 3.49
dayOldBreadPrice = 3.49 - (3.49 * 0.60)

totalBread = bread * breadPrice
totalDayOldBread = dayOldBread * dayOldBreadPrice
totalPrice = totalBread + totalDayOldBread

print('Your regular bread price is: ', totalBread)
print('Your day old bread price is: ', totalDayOldBread)
print('Your Total price is: ', totalPrice)