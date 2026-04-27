# 4. Date validation and increment
print("=== Program 4: Date Validation ===")
from datetime import datetime, timedelta
date_str = input("Enter date (YYYY-MM-DD): ")
try:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    print("Valid date!")
    incremented = date_obj + timedelta(days=1)
    print(f"Incremented date: {incremented.strftime('%Y-%m-%d')}")
except ValueError:
    print("Invalid date!")
print()
