def sum_d(n):
    t=0
    for i in range(1,n):
        if n%i==0:
            t+=i
    return t

n1=int(input("Enter A number:- "))
n2=int(input("Enter A number:- "))

sum1=sum_d(n1)
sum2=sum_d(n2)

if sum1==n2 and sum2==n1:
    print("Amicable")
else:
    print("No")