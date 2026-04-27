string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

unique_letters = []

for char in string1:
    if char not in string2 and char not in unique_letters:
        unique_letters.append(char)

print("Letters in first string but not in second:")
print(unique_letters)