def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series

# Test the functions
print("GCD of 48 and 18:", gcd(48, 18))
print("Factorial of 5:", factorial(5))
print("Fibonacci series (10 terms):", fibonacci(10))