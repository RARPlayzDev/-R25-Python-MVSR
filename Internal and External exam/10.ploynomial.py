coeff=list(map(int, input("Enter coeffcients(with spaces):-").split()))
x=int(input("Enter X value:-"))
p=len(coeff)-1
r=0
for c in coeff:
    r+= c*(x**p)
    p-=1
print(r)
