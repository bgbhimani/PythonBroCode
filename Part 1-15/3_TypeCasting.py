# Typecasting = The process to convert a variable from one data type to another
#  str(),int(),float(),bool()

name = "Bhavik"
age = 25
gpa = 5.5
is_student = True

# print(type(name))       # <class 'str'>
# print(type(age))        # <class 'int'>
# print(type(gpa))        # <class 'float'>
# print(type(is_student)) # <class 'bool'>

gpa = int(gpa)
age = float(age)
name = bool(name)
name2 = ""
name2 = bool(name2)


print(name2) # False if the String is is 0 length
print(name)  # True  No matter What in String
print(gpa)   # 5
print(age)   # 25.0

name = int(name)
print(name)   # 1
name3 = ""
name3 = int(name3)
print(name3)