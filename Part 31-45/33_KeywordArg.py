# keyword arguments=an argument preceded by an identifier
#                   helps with readability
#                   order of arguments doesn't matter
#                   1. positional 2. default 3.KEYWORD 4.arbitrary

def hello(greeting,title,first,last):
    print(f"{greeting} {title}{first}  {last}")

# hello("Hello","Mr.","Bhavik","Bhimani")
# hello("Hello",first="Bhavik",last="G",title="Sir,")

for x in range(1,11):
    print(x, end = " ") # Yes it's also the keyword Argument
print()
 
print("1","2","3","4","5",sep="-") # 1-2-3-4-5

def getphone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num = getphone(country=91,area=261,first=456,last=7890)

print(phone_num)
