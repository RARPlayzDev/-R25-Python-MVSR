l=[]
s=0
while True:
    n=int(input("Enter A number:-"))
    l.append(n)
    if n == 0:
        break
e=len(l)
for i in range(0,e-1):
    s+=l[i]
avg = s/e
print("Sum of list is:-",s)
print("Average of list is:-",avg)