def largest (a,b,c):
    if a>b and a>c:
        print(f"{a} is the largest number")
    elif b>a and b>c:
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")
x=int(input("Enter a Number:-"))
y=int(input("Enter a Number:-"))
z=int(input('Enter a Number:-'))
largest(x,y,z)