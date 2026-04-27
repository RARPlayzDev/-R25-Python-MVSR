# 13. Remove ith occurrence of word
print("=== Program 13: Remove ith Occurrence ===")
words = input("Enter words (space-separated): ").split()
target = input("Enter word to remove: ")
i = int(input("Enter occurrence number to remove: "))
count = 0
result = []
for word in words:
    if word == target:
        count += 1
        if count != i:
            result.append(word)
    else:
        result.append(word)
print(f"Result: {' '.join(result)}")
print()
