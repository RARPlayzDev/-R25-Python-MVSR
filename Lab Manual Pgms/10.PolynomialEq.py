'''A polynomial equation is an equation in which a polynomial is set equal to zero.
A polynomial is an expression consisting of variables and coefficients, that involves only the operations of addition, subtraction, multiplication, and non-negative integer exponents of variables.
For example, $x^2 - 5x + 6 = 0$$x^2 - 5x + 6 = 0$ is a polynomial equation.'''
"""
# 10. Compute polynomial equation with coefficients in list
print("=== Program 10: Polynomial Equation ===")
coefficients = list(map(float, input("Enter coefficients (space-separated): ").split()))
print(f"Coefficients stored in list: {coefficients}")
x = float(input("Enter value of x: "))
# Compute polynomial: coefficients[0]*x^n + coefficients[1]*x^(n-1) + ... + coefficients[n]
n = len(coefficients) - 1
result = sum(coefficients[i] * (x ** (n - i)) for i in range(len(coefficients)))
print(f"Polynomial result at x={x}: {result}")
print()
"""
coefficients = list(map(float, input("Enter the coefficients: ").split()))
x = float(input("Enter the value of x: "))

result = 0
n = len(coefficients) - 1   # highest power

for i in range(len(coefficients)):
    result += coefficients[i] * (x ** (n - i))

print("Result of the polynomial:", result)
