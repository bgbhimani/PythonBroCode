import random
options = ("Rock","Paper","Scissors")

playing = True
game = 0


while playing:

    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter Your Choice  = (Rock,Paper,Scissors): ")

    print(f"Your Choice: {player}")
    print(f"Computer choice: {computer}")
    game += 1

    if player == computer:
        print("It's Tie!!")
    elif player == "Rock" and computer == "Scissors":
        print("You Wins")
    elif player == "Paper" and computer == "Rock":
        print("You Wins")
    elif player == "Scissors" and computer == "Paper":
        print("You Wins")
    else: 
        print("The Computer Wins")

    if input("Like to play Again!!(y/n): ").lower() == 'n':
        playing = False
print(f"Total Games You Played: {game}")
print("Thanks for playing!!")