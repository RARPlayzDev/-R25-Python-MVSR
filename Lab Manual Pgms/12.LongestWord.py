print("=== Program 12: Longest Word from List ===")
n = int(input("How many words? "))
words_list = []
for i in range(n):
    word = input(f"Enter word {i+1}: ")
    words_list.append(word)
print(f"List of words: {words_list}")
longest = max(words_list, key=len)
print(f"Longest word: '{longest}'")
print(f"Length of longest word: {len(longest)}")
print()
