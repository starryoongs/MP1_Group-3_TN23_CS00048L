length = float (input("Enter the length in feet: "))
width = float (input("Enter the width in feet: "))

area_sqft = length * width
area_acres = area_sqft / 43560
 
print ("The area of the field is: ", area_acres, "acres.")