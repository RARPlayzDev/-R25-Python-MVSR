import random

# Generate two random numbers
a = random.randint(1, 50)
b = random.randint(1, 50)

print("Add the following numbers:")
print(a, "+", b)

# Student input
answer = int(input("Enter your answer: "))

# Check the answer
if answer == a + b:
    print("Congratulations! Your answer is correct.")
else:
    print("Wrong answer.")
    print("The correct answer is:", a + b)
