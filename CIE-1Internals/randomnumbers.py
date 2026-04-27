# 3. Disaply two random numbers that are to be added , the proram should allow the students to enter the answer.if the answer is correct,a message of congratualtions should be displayed,if the answer wrong"wrong" to be display

import random

a = random.randint(1, 50)
b = random.randint(1, 50)

print("Add:", a, "+", b)
answer = int(input("Enter your answer: "))

if answer == a + b:
    print("Congratulations! Correct answer.")
else:
    print("Wrong answer!")
