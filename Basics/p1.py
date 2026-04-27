num1=int(input("Enter A Number:- "))
if num1 % 3 == 0 and num1 % 5 == 0:
    print("Fizz Buzz")
elif num1 % 3 == 0:
    print("Fizz")
elif num1 % 5 == 0:
    print("buzz")
else:
    print("Invalid Input")
