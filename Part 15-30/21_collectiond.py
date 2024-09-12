# Collections: Single Variable used to store multiple Values  
#       List  :[] Ordered And Changable. Duplicate OK
#       Sets  :{} Unordered And Immutable. Add/Remove OK. No Duplicates
#       Tuples:() Orederd And Unchangable. Duplicates Ok Faster

#       #       #Tuples#        #       #
fruits = ("Apple","Oranges","Bananas","Coconut")
# print(dir(fruits))  #count and #index Methods Olny
# print(help(fruits))

print(fruits.index("Apple"))
print(fruits)       #('Apple', 'Oranges', 'Bananas', 'Coconut')
for a in fruits:
    print(a)



#       #       #List[]#        #       #
fruits = ["Apple","Oranges","Bananas","Coconut"]
# print(fruits[0])
# print(fruits[:3])
# print(fruits[::-1])    #For Reverse Print

# print(dir(fruits))  # Shows The Methods & Attributes In The Fruits Collection
# print(help(fruits))# detailes view of Mthd& attrbt

# print(len(fruits))    # 4 - return the length of the collection
# print("Apple" in fruits)  # True - return the available in the List or not
# fruits[0] = "PineApple"   # Changing the Value in the List
# fruits.append("Pineapple")  # Add the element at the End
# fruits.remove("Apple")  # Remove the Element
# fruits.insert(0,"Pineapple")
# fruits.sort()     # Sort Aplphabatically
# fruits.reverse()   #Reverse As we had Placed Elements``
# fruits.clear()   # All Elements Are Gone
# print(fruits.index("Coconut"))  # 3
# fruits.append("Bananas")
# print(fruits.count("Bananas"))    # 2

# for x in fruits:
    # print(x,end=" ")



#       #       #Sets#      #       #
fruits = {"Apple","Orange","Banana","Coconut"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("Pineapple" in  fruits)   # False
# fruits.add("Pineapple")
# fruits.remove("Pineapple")
# fruits.pop()   # Remove the first element althought it is random
# fruits.clear()
# fruits.add("Apple")
