'''A strong number is a number such that the sum of the factorial of its digits is equal to the number itself. For example, 145 is a strong number because
$1! + 4! + 5! = 1 + 24 + 120 = 145$$1! + 4! + 5! = 1 + 24 + 120 = 145$.'''

# 9. Check for strong number
print("=== Program 9: Strong Number ===")
import math
num = int(input("Enter a number: "))
digit_sum = sum(math.factorial(int(d)) for d in str(num))
if digit_sum == num:
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")
print()
