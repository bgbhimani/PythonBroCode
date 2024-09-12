# 2D Lists

fruits = ["Apple","Banana","Oranges","Coconut"]
vegetables = ["Carrot", "Onion","Potato","Tomato"]
grains = ["Wheat","Rice","Corn"]

# groceries = [fruits, vegetables, grains]
groceries = [["Apple","Banana","Oranges","Coconut"],
             ["Carrot", "Onion","Potato","Tomato"],
             ["Wheat","Rice","Corn"]]


# print(groceries)  #[['Apple', 'Banana', 'Oranges', 'Coconut'], ['Carrot', 'Onion', 'Potato', 'Tomato'], ['Wheat', 'Rice', 'Corn']]
# print(groceries[1])  # ['Carrot', 'Onion', 'Potato', 'Tomato'] 
# print(groceries[0][0])  # Apple


# for collection in groceries:
#     for food in collection:
#         print(food, end = " ")
    # print()



# Exceries: print keypad 1 to 0
keypad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ('*',0,'#'))

for row in keypad:
    for col in row:
        print(col,end = " ")
    print()