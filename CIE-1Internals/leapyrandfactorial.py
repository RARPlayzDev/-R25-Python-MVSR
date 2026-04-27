# 8. Leap year/factorial o f num using recursion

year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

num = int(input("Enter number: "))
print("Factorial =", fact(num))
