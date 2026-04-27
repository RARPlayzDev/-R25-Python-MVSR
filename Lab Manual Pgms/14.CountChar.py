# 14. Count character types in sentence (without functions)
print("=== Program 14: Count Character Types ===")
sentence = input("Enter a sentence: ")
alphabets = 0
consonants = 0
vowels = 0
digits = 0
special = 0

vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for char in sentence:
    # Check if character is an alphabet
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        alphabets += 1
        # Check if vowel or consonant
        if char in vowel_list:
            vowels += 1
        else:
            consonants += 1
    # Check if character is a digit
    elif char in digit_list:
        digits += 1
    # Check if not space (then it's special character)
    elif char != ' ':
        special += 1

print(f"Alphabets: {alphabets}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Special characters: {special}")
print()
