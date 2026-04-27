total = 0
numbers = input("Enter numbers separated by space: ").split()

for num in numbers:
    total += int(num)

print("Sum of the given numbers =", total)
