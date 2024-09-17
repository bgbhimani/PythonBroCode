# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
# for x in range(1,11):
#     doubles.append(x*2)
# print(doubles)

# doubles = [x * 2  for x in range(1,11) ] 
# triples = [y * 3  for y in range(1,11) ]
# print(doubles)   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(triples)   # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# fruits = ["Apple","Banana","Pear","Mango"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)  # ['APPLE', 'BANANA', 'PEAR', 'MANGO']

# numbers = [-5,2,6,-5,-8,-1,7,6,3,4]
# positive_num = [num for num in numbers if num>0 ]
# print(positive_num)     # [2, 6, 7, 6, 3, 4]
# negative_num = [num for num in numbers if num<0 ]
# print(negative_num)     # [-5, -5, -8, -1]

grades = [85,62,82,74,26,85,96,15,24,59,69]
pass_grad = [grade for grade in grades if grade>60]
print(pass_grad)     # [85, 62, 82, 74, 85, 96, 69]