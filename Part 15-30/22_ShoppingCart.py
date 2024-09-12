foods = []
prices = []
total = 0

while True:
    food = input("Enter The Foo to Buy (q for Quit): ")
    
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter The Amount of the {food} : ₹"))
        prices.append(price)
        foods.append(food)
    
print("\n----- Your Cart -----")
for food in foods:
    print(food,end = " ")

for price in prices:
    total += price

print(f"\nTotal Price: ₹{total:.2f} ")