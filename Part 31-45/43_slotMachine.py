import random

def spin_row():
    symbols =["🍒","🍉","🍋","🔔","⭐"]
    return [random.choice(symbols) for _ in range(3)]



def print_row(row):
    print("*******************")
    print("  |  ".join(row))
    print("*******************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet*3
        elif  "🍉":
            return bet*5
        elif  "🍋":
            return bet*10
        elif  "🔔":
            return bet*20
        elif  "⭐":
            return bet*30
    else: 
        return 0

def main():
    balance = 100
    print("*******************")
    print("Welcome to the Python Slots.")
    print("symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*******************")

    while balance>0:
        print(f"Current balance is {balance}₹")
    
        bet = input("Place your bet Amount: ")

        if not bet.isdigit():
            print("Ente Valid Input.")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("Insufficent Funds")
            continue

        if bet <= 0:
            print("It must be grater than 0")
            continue

        balance -= bet

        row  = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)
        
        if payout > 0:
            print(f"Congratulations! you Won₹{payout}")
        else:
            print("Youe had Lost!!")
        
        balance += payout

        play_again = input("Whould you like to spin again?? (y/n)").lower()
        if play_again == "y":
            continue
        else:
            print(f"Thanks for playing. Your final balance is {balance}₹")
            break


if __name__ ==  "__main__":
    main()