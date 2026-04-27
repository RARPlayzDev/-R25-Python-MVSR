# 2. Read numbers from command line and add them
print("=== Program 2: Add Command Line Numbers ===")
import sys
if len(sys.argv) > 1:
    numbers = [float(x) for x in sys.argv[1:]]
    print(f"Sum: {sum(numbers)}")
else:
    nums = input("Enter numbers separated by space: ").split()
    total = sum(float(x) for x in nums)
    print(f"Sum: {total}")
print()


"""
# 2. read a set of numbers from the command line, add and print those numbers

numbers = input("Enter numbers separated by space: ").split()
total = 0

for num in numbers:
    total += int(num)

print("Sum =", total)

"""