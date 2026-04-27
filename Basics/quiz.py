# Program to ask 5 questions and keep score

def quiz():
    score = 0

    ans = input("1. Capital of India? ")
    if ans.lower() == "new delhi":
        score += 1

    ans = input("2. Color of the sky? ")
    if ans.lower() == "blue":
        score += 1

    ans = input("3. 2 + 2 = ? ")
    if ans == "4":
        score += 1

    ans = input("4. Opposite of hot? ")
    if ans.lower() == "cold":
        score += 1

    ans = input("5. How many days in a week? ")
    if ans == "7":
        score += 1

    print("Your score is:", score, "out of 5")

quiz()
