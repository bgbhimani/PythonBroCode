import random

high = 0
low = 100
# number = random.randint(1,6)
# number = random.randint(low,high)
number = random.random()  #Random Float


options = ("Rock","Paper","Scissors")
option = random.choice(options)

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
card = random.choice(cards)
random.shuffle(cards)   #suffle the collection elements


print(cards)
# print(option)
# print(number)
