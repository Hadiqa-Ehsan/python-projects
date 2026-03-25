questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "How many continents are there?"
]
answers = [
    "Paris",
    "Mars",
    "7"
]
score = 0

for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ")
    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print("Quiz Finished!")
print("Your score is:", score, "out of", len(questions))