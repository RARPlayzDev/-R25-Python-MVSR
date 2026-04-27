# 4. read date and check whether the date is valid or not

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid Date")
else:
    if month in [1,3,5,7,8,10,12]:
        max_day = 31
    elif month in [4,6,9,11]:
        max_day = 30
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            max_day = 29
        else:
            max_day = 28

    if day >= 1 and day <= max_day:
        print("Valid Date")
    else:
        print("Invalid Date")
