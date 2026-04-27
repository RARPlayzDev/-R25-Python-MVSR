def compute_gcd(a, b): 
    """ 
    Computes the greatest common divisor (GCD) of two integers using the  Euclidean algorithm. 
    """ 
    while b: 
        a, b = b, a % b 
    return a 
 
num1 = 56 
num2 = 98 
print(f"The GCD of {num1} and {num2} is: {compute_gcd(num1, num2)}")
 
def factorial_iterative(n): 
    """Computes the factorial of n using an iterative approach.""" 
    if n < 0: 
        return "Error: Factorial is not defined for negative numbers" 
    result = 1 
    for i in range(1, n + 1): 
        result *= i 
    return result 
 
 
# Example usage: 
print(f"5! (iterative): {factorial_iterative(5)}") 
print(f"0! (iterative): {factorial_iterative(0)}") 
 
def fibonacci_series_iterative(n_terms): 
    """Generates the Fibonacci series up to n_terms using an iterative approach.""" 
    if n_terms <= 0: 
        return "Error: Number of terms must be positive" 
     
    a, b = 0, 1 
    count = 0 
    result = [] 
    while count < n_terms: 
        result.append(a) 
        a, b = b, a + b 
        count += 1 
    return result 
 
# Example usage: 
print(f"Fibonacci series (10 terms, iterative): {fibonacci_series_iterative(10)}")