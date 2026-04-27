n=int(input("Enter a number: "))
a=list(map(int,input("Enter the elements: ").split()))

l=0
r=n-1
s=0
d=0
t=0
while l<=r:
    if a[l]>a[r]:
        x=a[l]
        l+=1
    else:
        x=a[r]
        r-=1
    if t==0:
        s+=x
    else:
        d+=x
    t=1-t
print(s,d)