s=input("Enter A String:-")
l=len(s)
for i in range(l-1,-1,-1):
    print(s[i])
x=l-1
while x>=0:
    print(s[x])
    x-=1
