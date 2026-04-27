def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

n1=int(input("Enter A number:- "))
temp =n1
sum=0
while temp>0:
    digit=temp%10
    sum+=factorial(digit)
    temp //=10
if sum == n1:
    print('Strong')
else:
    print("No")