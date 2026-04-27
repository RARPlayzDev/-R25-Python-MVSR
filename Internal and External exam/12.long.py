words=list(map(str, input("Enter words separated by spaces:-").split()))
longest=0
for word in words:
    if len(word)>longest:
        longest=len(word)
print(f"length of longest word is:-{longest}")