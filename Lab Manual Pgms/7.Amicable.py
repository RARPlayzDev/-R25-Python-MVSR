'''Amicable numbers are two different numbers such that the sum of the proper divisors of each is
equal to the other number. A proper divisor of a number is a divisor of the number,
other than the number itself. For example, 220 and 284 are amicable numbers.
The proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110, which sum to 284.
The proper divisors of 284 are 1, 2, 4, 71, and 142, which sum to 220.'''

# 7. Check for amicable numbers
print("=== Program 7: Amicable Numbers ===")
def sum_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

num = int(input("Enter a number: "))
partner = sum_divisors(num)
if sum_divisors(partner) == num and num != partner:
    print(f"{num} and {partner} are amicable numbers")
else:
    print(f"{num} is not an amicable number")
print()
