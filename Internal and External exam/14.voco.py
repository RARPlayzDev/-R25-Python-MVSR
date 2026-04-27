sentence = input("Enter a sentence: ")

alphabets = 0
vowels = 0
consonants = 0
digits = 0
special = 0

vowel_list = "aeiouAEIOU"

for char in sentence:
    if char.isalpha():
        alphabets += 1
        if char in vowel_list:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    else:
        special+=1

print(f"Alphabets: {alphabets}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Special characters: {special}")