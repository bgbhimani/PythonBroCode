#input() = a function that prompts the user to enter data Returns the Entered data as a String

name = input("What is your name: ")
age = int(input("How old are you? :"))
age = age+1

print(f"Hello {name}!")
print(f"You are {age} years old!")