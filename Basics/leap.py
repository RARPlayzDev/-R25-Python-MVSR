y=int(input("Enter A Year:- "))
if y % 400 == 0 :
    print(y ,"Is a leap year")

elif y % 100 == 0:
    print(y ,"Its a leap year")
        
elif y % 4 ==0:
    print(y ,"Its a leap year")

else:
    print("Invalid year")