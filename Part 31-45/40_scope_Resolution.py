# variable scopel - where a variable is visible and accessible
# scope resolution - (LEGB) Local -> Enclosed and accessible - > Global - > Built-in

# def fun1():
#     x = 1 
#     print(x)
    
# def fun2():
#     x = 2
#     print(x)

# fun1()
# fun2()  # Here Both X are local

# def fun1():
#     x = 1 
#     def fun2():
#         print(x)
#     fun2()
# fun1()  # here the x is enclosed and and accessible

# def fun1():
#     print(x)
# def fun2():
#     print(x)
# x = 2
# fun1()
# fun2()  # here the x is globle variable

# from math import e
# def fun1():
#     print(e)
# e=3
# fun1()  # here math.e = 2.71.... but in order it uses the global first

