# 9. Count Down /Swapping of two numbers

import time

n = int(input("Enter a number to count down: "))

for i in range(n, -1, -1):
    print(i)
    time.sleep(1)     # 1 second gap

a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a
print("After swap: a =", a, "b =", b)
