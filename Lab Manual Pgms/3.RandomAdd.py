# 3. Random number addition quiz
print("=== Program 3: Random Number Quiz ===")
import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
print(f"What is {num1} + {num2}?")
answer = int(input("Your answer: "))
if answer == num1 + num2:
    print("Congratulations! Correct answer.")
else:
    print(f"Wrong! Correct answer is {num1 + num2}")
print()

