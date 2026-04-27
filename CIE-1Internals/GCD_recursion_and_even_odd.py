# 13. WAP to find GCD of num using recursion /even and Odd

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("GCD =", gcd(a, b))

num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
