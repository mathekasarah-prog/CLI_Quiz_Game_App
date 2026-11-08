import random

questions = [
    {
        "question": "What is the capital city of Kenya?",
        "choices": {
            "A": "Mombasa",
            "B": "Nairobi",
            "C": "Kisumu",
            "D": "Nakuru"
        },
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "choices": {
            "A": "Python",
            "B": "Java",
            "C": "JavaScript",
            "D": "C++"
        },
        "answer": "C"
    },
    {
        "question": "What is 10 * 5?",
        "choices": {
            "A": "40",
            "B": "45",
            "C": "50",
            "D": "60"
        },
        "answer": "C"
    }
]

# Mix the questions
random.shuffle(questions)

# Initialize score
score = 0


# Loop through questions
for question in questions:

    print("\n" + question["question"])

    for letter, choice in question["choices"].items():
        print(f"{letter}. {choice}")

    user_answer = input("Enter your answer (A, B, C, D): ").upper()

    if user_answer not in ["A", "B", "C", "D"]:
        print("Invalid answer!")
        continue

    if user_answer == question["answer"]:
        print("Correct! Well done.")
        score += 1
    else:
        print("Wrong answer!")
        print(f"The correct answer is {question['answer']}")

# Final results
print("\n================================")
print("          QUIZ RESULTS")
print("================================")

print(f"Your score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

if percentage >= 80:
    print("Excellent!")
elif percentage >= 50:
    print("Good job!")
else:
    print("Try Again!")
