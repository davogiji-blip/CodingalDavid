import datetime
import calendar

city = input("Enter a city : ")
temp = float(input("Enter a temperature: "))

if temp > 35:
    print("Warning")

elif temp > 25:
    print("Warm and Sunny")
else:
    print("Good Weather")

date1 = datetime.datetime.now()
print(date1)

calendar1 = calendar.month(2026, 6)
calendar2 = calendar.calendar(date1.year)
print(calendar1)
print(calendar2)