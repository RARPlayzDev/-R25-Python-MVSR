# Input from user
n = int(input("Enter a number: "))
is_prime=True
for i in range(1,int(n*0.5)+1):
    if n%2==0:
        is_prime=False
if is_prime:
    print("Prime")
else:
    print("False")
