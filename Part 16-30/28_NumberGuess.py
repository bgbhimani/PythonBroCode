import random

low = 1
high = 10
answer = random.randint(low,high)

guesses = 0
is_running = True

print("The Number Guessing Game:")
print(f"Select the number Bteween {low} and {high}")

while is_running:
    guess = (input("Enter the Number: "))
    
    if guess.isdigit():
        guess = int(guess)  
        guesses += 1
        
        if guess<low or guess>high:
            print("The Number is Out of range")
            print(f"choos between {low} to {high}.")
        elif guess<answer:
            print("Your Guess is Low!! Try Again with Higher")
        elif guess>answer:
            print("Your Guess is high. Try the small number")
        elif guess == answer:
            print(f"""
                  Hurray!!! You won the Game!!
                  Your Total guesses is {guesses}""")
            is_running = False
    

    else:
        print("Invlid guess")
        print(f"choos between  {low} to {high}.")
