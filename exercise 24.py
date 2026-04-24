days = int(input("Enter number of days: "))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

days_seconds = days * 86400
hours_seconds = hours * 3600
minutes_seconds = seconds * 60
seconds_seconds = seconds

total_seconds = days_seconds + hours_seconds + minutes_seconds + seconds_seconds

print(total_seconds)