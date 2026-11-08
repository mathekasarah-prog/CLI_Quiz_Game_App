import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": {"A) Berlin",
                    "B) Madrid",
                    "C) Paris", 
                    "D) Rome"},
        "answer": "C) Paris"
    
},
    {
        "question": "What is the largest planet in our solar system?",
        "options": {"A) Earth",
                    "B) Jupiter",
                    "C) Saturn",
                    "D) Mars"},
        "answer": "B) Jupiter"
    },
    
    {
            "question": "What is the chemical symbol for gold?",
            "options": {"A) Au",
                        "B) Ag",
                        "C) Fe",
                        "D) Hg"},
        "answer": "A) Au"
                        

    }
    
    ]

random.shuffle(questions)
print(questions)


score = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer (A, B, C, or D): ")
    if answer.upper() == q["answer"][0]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is {q['answer']}.")
print(f"Your final score is {score}/{len(questions)}.")


#final results
print("\n================================")
print("          QUIZ RESULTS")
print("================================")

print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

if percentage >= 80:
    print("Excellent! You passed the quiz.")
    
elif percentage >= 50:
    print("Good job! You passed the quiz.")
    
else:
    print("You did not pass the quiz. Better luck next time!")