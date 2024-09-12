# Dictionary: a collection of {key:value} pair
#             Ordered And Changable. No Duplicates

capitals = {"India":"Delhi",
           "Nepal":"Kathmandu",
           "Japan": "Tokyo",
           "USA":"Washington D.C."}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("India"))   # Delhi
# print(capitals.get("China"))   # None 
# 
# if capitals.get("china"):
    # print("That Capital Exist..")
# else: 
    # print("That Capital Doesn't Exist..")

capitals.update({"Germany":"Berlin"})
capitals.update({"India":"New Delhi"})
# capitals.pop("USA")
# capitals.popitem()  # It will remove the Letast item
# capitals.clear()

# Keys = capitals.keys()
# print(Keys)  # dict_keys(['India', 'Nepal', 'Japan', 'USA', 'Germany'])
# for keys in capitals.keys():
#     print(keys)

# Val = capitals.values()
# print(Val)  # dict_values(['New Delhi', 'Kathmandu', 'Tokyo', 'Washington D.C.', 'Berlin'])
# for value in capitals.values():
#     print(value)

# item = capitals.items()

for key , value in capitals.items():
    print(f"{key} : {value}")