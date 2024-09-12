#  While : some code execute while some condition remains true

# name  = input("Enter Your Name: ")
# while name == "":
#     print("Name cannot be empty")
#     name = input("Enter Your Name: ")
# print(f"Hello, {name}")


age = int(input("Enter Your Age:"))
while age < 0 :
    print("Age cannot be negative")
    age = int(input("Enter Your Age:"))
print(f"Youe Are {age:} years old ")