def gcd(a, b): 
        if (b == 0):  
              return a 
        else:  
             return gcd(b, a % b) 
print("GCD Of  56,98 is ",gcd(56,98)) 
# Python 3 program to find   
# factorial of given number  
def factorial(n):  
     # Checking the number is 1 or 0 then return 1 other wise return factorial 
    if (n==1 or n==0): 
        return 1 
    else: 
        return (n * factorial(n - 1))  
num = 5
print("number : ",num) 
print("Factorial : ",factorial(num)) 
 
# Recursive Function for Fibonacci number 
def Fibonacci(n): 
    if n<= 0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n == 1: 
        return 0 
    # Second Fibonacci number is 1 
    elif n == 2: 
        return 1 
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
print(Fibonacci(10))