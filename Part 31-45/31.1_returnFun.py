# return = statement used to end a function 
#          and send a result back to the caller

def add(x,y):
    z = x+y
    return z

def sub(x,y):
    z = x-y
    return z

def multiply(x,y):
    z = x*y
    return z

def division(x,y):
    z = x/y
    return z

print("The Addition      : ",add(1,2))
print("The Substracion   : ",sub(1,2))
print("The Multiplication: ",multiply(1,2))
print("The Division      : ",division(1,2))

def createFullName(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " +last

full_name = createFullName("bhavik","bhimani")
print(full_name )