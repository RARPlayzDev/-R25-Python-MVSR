# Validate and increment date

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

# Days in each month
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Check for leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_month[1] = 29

# Validate date
if month < 1 or month > 12:
    print("Invalid month!")
elif day < 1 or day > days_in_month[month - 1]:
    print("Invalid day!")
else:
    print(f"Valid date: {day}/{month}/{year}")
    
    # Increment date
    day += 1
    if day > days_in_month[month - 1]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    
    print(f"Incremented date: {day}/{month}/{year}")