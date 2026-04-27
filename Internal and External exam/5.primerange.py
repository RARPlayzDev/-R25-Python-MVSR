x = int(input("Enter x: "))
y = int(input("Enter y: "))

print("Prime numbers between", x, "and", y, "are:")

for num in range(x, y + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
