def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test the functions
print("GCD of 48 and 18:", gcd_recursive(48, 18))
print("Factorial of 5:", factorial_recursive(5))
print("10th Fibonacci number:", fibonacci_recursive(10))