text = input("Enter a sentence: ").lower()

words = text.split()
w_c = {}

for word in words:
    word = word.lower()
    if word in w_c:
        w_c[word] += 1
    else:
        w_c[word] = 1

print("Word Count:")
for word, count in w_c.items():
    print(word, ":", count)
