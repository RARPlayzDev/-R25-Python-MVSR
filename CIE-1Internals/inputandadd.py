# 2. read a set of numbers from the command line, add and print those numbers

numbers = input("Enter numbers separated by space: ").split()
total = 0

for num in numbers:
    total += int(num)

print("Sum =", total)
