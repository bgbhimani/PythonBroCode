# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

# word = "apple"
# letter = input("Guess A letter in the secret word: ")
# if letter in word:
#     print(f"There is a {letter} ")
# else:
#     print(f"{letter} was not found ")

# students = {"bgb", "dhuv", "agb"}
# student = input("Enter the name of student: ")
# if student in students:
#     print(f"{student} found in set")
# else:
#     print(f"{student} was not found.")

# grades = {"bgb":"A","agb":"B","dhruv":"C"}
# student = input("Enter the name of student: ")
# if student in grades:
#     print(f"{student}'s grad is {grades[student]}")
# else:
#     print(f"{student} was not found")

email = "bgb.@fakemail.com"
if "@" in email and "." in email:
    print(f"Valid Email")
else:
    print("invalid email")