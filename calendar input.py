import calendar

year= int(input("enter year: "))
month= int(input("enter month: "))

if 1 <= month <= 12:
   print(calendar.month(year, month))
else:
   print("invalid number! press between 1 to 12")