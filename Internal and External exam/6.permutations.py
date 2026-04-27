from itertools import permutations
digits = input("Enter three digits (space separated): ").split()
print("All possible combinations are:")
for p in permutations(digits):
    print("".join(p))