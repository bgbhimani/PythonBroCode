
def show_balance(balance):
    print("*******************")
    print(f"Your Balance is ₹{balance:.2f}")

def deposite(balance):
    print("*******************")
    amount = float(input("Enter the amount to deposite: "))
    if amount<0:
        print("*******************")
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    print("*******************")
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("*******************")
        print("Low Balance You can't Withdraw")
        return 0
    elif amount<0:
        print("*******************")
        print("Invalid Amount.")
        return 0
    else:
        return amount
    

def main():
    balance = 0
    is_running = True

    while True:
        print("*******************")
        print("Banking Programme")
        print("*******************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*******************")
        choice = int(input("Enter Your Choice(1-4):"))
        match choice:
            case 1: show_balance(balance)
            case 2: balance += deposite(balance)
            case 3: balance -= withdraw(balance)
            case 4: exit()
            case _:
                print("*******************")
                print("Enter Valid Input")

    print("*******************")
    print("Thank You!! have a nice Day")
    print("*******************")

if __name__ =="__main__":
    main()