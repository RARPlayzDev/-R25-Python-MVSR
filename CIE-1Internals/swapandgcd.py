# 7. Swapping of two numbers using temp variable /GCD of a number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a,b=b,a
print("After swap: a =", a, "b =", b)

x, y = a, b
while y != 0:
    x, y = y, x % y
print("GCD =", x)
