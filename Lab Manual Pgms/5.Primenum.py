# 5. Read x,y and print all prime numbers between x and y where x<=y
print("=== Program 5: Prime Numbers ===")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

x = int(input("Enter x: "))
y = int(input("Enter y: "))

# Validate that x <= y
if x > y:
    print("Error: x should be less than or equal to y")
else:
    print(f"Prime numbers between {x} and {y}:")
    primes = []
    for num in range(x, y+1):
        if is_prime(num):
            primes.append(num)
    
    if primes:
        print(primes)
    else:
        print("No prime numbers found in this range")
print()
