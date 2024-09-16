# default arguments =A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces no. of arguments
#                    1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

import time

# def net_price(list_price, discount=0 ,tax=0.5):
#     return list_price*(1-discount)*(1+tax)

# # net_price(500) It Gives Error
# print(net_price(500))
# print(net_price(500,0.1))


def count(end,start=0):
    for x in range (start,end+1):
        print(x)
        time.sleep(1)
    print("Done!!")

count(10)