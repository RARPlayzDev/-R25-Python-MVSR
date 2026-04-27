# 11. Count occurrences in list
print("=== Program 11: Count Occurrences ===")
numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
target = int(input("Enter number to search: "))
count = numbers.count(target)
print(f"{target} occurs {count} times")
print()
