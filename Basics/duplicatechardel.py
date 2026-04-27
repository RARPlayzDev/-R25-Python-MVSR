s=input("Enter A String:-")
dup=""
for char in s:
    char_low=char.lower()
    if char_low not in dup:
        dup+=char_low
print("String without Duplicate:-",dup)