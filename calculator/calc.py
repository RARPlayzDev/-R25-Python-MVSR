a = float(input("Enter A Number:- "))
b = float(input("Enter A Number:- "))
print("1.To add")
print("2.To Subtract")
print("3.To Multiply")
print("4.To divide")
c = int(input("Enter Your choice:- "))

match c:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        if b != 0:
            print(a/b)
        else:
            print("Cannot perform the given operation")
    case 5:
        print("Option not found")
    