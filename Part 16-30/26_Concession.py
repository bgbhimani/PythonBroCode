# The Concession Progrrame
# Store At the Movie Thetares

menu = {"pizza": 60.25,
        "nachos": 15.25,
        "popcorn":20.15,
        "fries": 62.23,
        "soda" : 15.23,
        "chips" : 25.24,
        "samosa": 52.32
        }

cart =[]
total = 0

print("-------- Menu --------")
for key, value in menu.items():
    print(f"{key:10}: ₹{value:.2f}")
print("----------------------")

while True:
    food = input("Select an item (q for Quit): ").lower()
    if food == "q" :
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---- Your Order ----")
for food in cart:
    total +=  menu.get(food)
    print(food , end=" ")
print(f"\nTotal : ₹{total:.2f} ")