s = input("Enter a string: ")

vowels = "aeiouAEIOU"
distinct = ""     

for ch in s:
    if ch in vowels:
        ch_low = ch.lower()     
        if ch_low not in distinct:
            distinct += ch_low    

print("Distinct vowels:", distinct)
