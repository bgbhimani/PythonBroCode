# *args    = allows you to pass multiple non-key arguments 
# **kwargs = allows you to pass multiple keyword-arguments 
#            *unpacking operator
# 1. positional 2. default 3.keyword 4.ARBITRARY 

# def add(*args):  # Us when more arg give in callin function
#     total = 0                       # if use *args it stors the args in tuple
#     for arg in args:                # we can change the name like *nums
#         total += arg                # but * is important
#     return total
# print(add (6,6,6,6,6))


# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
# display_name("Mr.","Bhavik")

# def print_address(**kwargs):
#     # print(type(kwargs))    # <class 'dict'>
#     for keys,value in kwargs.items():
#         print(f"{keys:6} :  {value}")
# print_address(street="123 Fake Street",
#               city="Surat", state="Gujarat",
#              zip="394105")


def shipping_lable(*args,**kwargs):
    for arg in args:
        print(arg,end =" ")
    print()
    # for key,val in kwargs.items():
    #     print(f"{key:7} : {val}")
    
    if "aprtment" and "Street" in kwargs:
        print(f"{kwargs.get('Street')} {kwargs.get('aprtment')}" )
    if "City" and "state" in kwargs:
        print(f"{kwargs.get('City')} {kwargs.get('state')}")




shipping_lable("Mr.","Bhavik","Bhimani",
               Street = "Sai Avenue", City = "Surat", state="Gujarat")