# function = A block of reusable code
#            place () after the function name to invoke it
# Positional Arguments
def HappyBirthday():
    print("Happt BirthDay!!")
    print("You're Getiing Old!!")
    print()
HappyBirthday()

def HappyBirthday2(name):
    print(f"Happt BirthDay {name}!!")
    print("You're Getiing Old!!")
    print()
HappyBirthday2("Bhavik")

def HBD3(name,age):
    print(f"Happy B'day!! {name}")
    print(f"Your Are {age+1} now")
    print()
HBD3("BhavikG",18)

def display_invoice(username, amount, dueDate):
    print(f"Hello!!  {username}")
    print(f"Your bill of ₹{amount:.2f} is due at {dueDate}")

display_invoice("Bhavik",25.636,"01/01")