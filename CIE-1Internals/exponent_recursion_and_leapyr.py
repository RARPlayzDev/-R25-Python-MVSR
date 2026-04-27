# 14. Find exponents of num using recursion /leap year

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Result =", power(base, exp))

year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
