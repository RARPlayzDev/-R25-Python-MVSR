num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Factorial
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)
