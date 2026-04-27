s = input("Enter the string: ")
result = ""
i = 0
while i < len(s):
    ch = s[i]      
    i += 1
    count = ""     
    while i < len(s) and s[i].isdigit():
        count += s[i]
        i += 1
    result += ch * int(count)  
print(result)
