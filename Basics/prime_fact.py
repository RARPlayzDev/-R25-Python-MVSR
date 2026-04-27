# Program to print prime factors of a number

num = int(input("Enter a number: "))

print("Prime factors are:", end=" ")

i = 2
while num > 1:
    if num % i == 0:
        print(i, end=" ")
        num = num // i
    else:
        i = i + 1
