# Quiz Question

questions = (
            "Highest Mountain in the World",
            "How many Elements are in the periodic table?",
            "Which Animal lays Biggest eggs",
            "Which month have Only 28 Days",
            "2 + 2 = (?)")

options = (
          ("A. Mt.Abu","B. Mt.Everest","C. Mt.Fuji","D. Mt.K2"),
          ("A.116","B.117","C.118","D.119"),
          ("A.Whale","B.Elephant","C.Ostrich","D.Crocodile"),
          ("A.June","B.July","C.Fab","D.December"),
          ("A.5","B.8","C.25","D.4"))

answers = ("B","D","C","C","D") 
guesses = []
score = 0
QuestionNum = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[QuestionNum]:
        print(option)

    guesse = input("Enter (A,B,C,D): ").upper()
    guesses.append(guesse)
    if guesse == answers[QuestionNum]:
        score += 1 
        print("Correct")
    else:
        print("Incrreoct")
        print(f"{answers[QuestionNum]} is the Correct Answer")

    QuestionNum += 1


print("---------")
print(" Result  ")
print("---------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int((score/len(questions)) * 100) 
print(f"Your Final Score: {score}%")