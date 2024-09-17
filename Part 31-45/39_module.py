# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# print(help("modules")
# import math
# import mats as m

# from math import e
# print(e)   # 2.718281828459045
# a,b,c,d,e = 1,2,3,4,5
# print(e**b)   # 25

import example

result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.circumference(5)
result = example.area(4)

print(result)  