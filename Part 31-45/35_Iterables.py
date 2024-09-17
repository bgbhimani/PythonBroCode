# Iterables = An object/ collection that can return its elements one at a 
#             time, allowing it to be iterated over in a loop


# numbers = [1,2,3,4,5,6,7]
# for num in reversed(numbers):
#     print(num,end =" ")

# String
# name = "Bhavik Bhimani"
# for char in name:
#     print(char,end="")

# Dictionary
my_dictionary = {"A":1,
                 "B":2,
                 "C":3,
                 "D":4}

for key,value in my_dictionary.items():
    print(f"{key:2} : {value}")