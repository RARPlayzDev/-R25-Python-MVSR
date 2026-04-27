# 12. fibonacci series using iteration and recursion

n = int(input("How many terms? "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci using recursion:")
for i in range(n):
    print(fib(i))
