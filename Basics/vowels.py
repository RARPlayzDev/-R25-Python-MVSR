s = input("Enter A String:- ")
v="aeiouAEIOU"
count=0
counts=0
for char in s:
    if char in v:
        count+=1
    else:
        counts+=1
print("No' of Vowels in the string:-",count)
print("No' of Consonents in the string:-",counts)