string1 = "programming" 
string2 = "language" 
result = [ ] 
for char in string1: 
    if char not in string2 and char not in result: # Check for uniqueness in result list 
        result.append(char) 
print(f"Letters in the first string but not in the second (ordered): {result}") 