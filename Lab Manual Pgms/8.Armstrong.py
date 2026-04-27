'''An Armstrong number (also known as a narcissistic number) is a number
that is the sum of its own digits each raised to the power of the number of digits.
For example, 153 is an Armstrong number because it has 3 digits,
and $1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$$1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$.'''

# 8. Check for Armstrong number
print("=== Program 8: Armstrong Number ===")
num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
power = len(digits)
armstrong_sum = sum(d**power for d in digits)
if armstrong_sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
print()

