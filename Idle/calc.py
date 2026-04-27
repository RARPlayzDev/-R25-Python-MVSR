#10 Basic Calculator
a = int(input("Enter a number:- "))
b = int(input("Enter a number:- "))
op = input("Enter operator +, -, *, /:- ")

if op == '+':
    print("Sum =", a + b)
elif op == '-':
    print("Difference =", a - b)
elif op == '*':
    print("Product =", a * b)
elif op == '/':
    if b!=0:
        print("Divison =",a/b)
    else:
        print("Cannot Perform the Operation")
else:
    print("Invalid inputs")
