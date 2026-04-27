# QUIZ PROGRAM USING ONLY LISTS

questions = [
    "1. What is the capital of India?",
    "2. Who developed Python?",
    "3. Which data type is mutable?",
    "4. Which one is a logical operator?"
]

options = [
    ["A) Mumbai B) Delhi C) Kolkata D) Chennai"],
    ["A) Guido van Rossum", "B) Elon Musk", "C) Sundar Pichai", "D) Bill Gates"],
    ["A) Tuple", "B) String", "C) List", "D) Integer"],
    ["A) AND", "B) OR", "C) NOT", "D) All of the above"]
]

# Correct answers (using letters)
answers = ["B", "A", "C", "D"]

score = 0

print("\n*** WELCOME TO THE QUIZ ***\n")

# Loop through the questions
for i in range(len(questions)):
    print(questions[i])
    for opt in options[i]:
        print(opt)
    
    user_ans = input("Your Answer (A/B/C/D): ").strip().upper()

    if user_ans == answers[i]:
        print("✔ Correct!\n")
        score += 1
    else:
        print(f"✘ Wrong! Correct answer is: {answers[i]}\n")

print("Quiz Completed!")
print(f"Your Final Score: {score}/{len(questions)}")
