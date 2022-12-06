# leap year 
year=float(input("Enter a year to verify: "))
if year % 4==0 and year % 100 != 0:
    print("Is a leap year")
elif year % 4==0 and year % 100 == 0 and year%400==0:
        print("Is a leap year")
else:
    print("No Leap year")