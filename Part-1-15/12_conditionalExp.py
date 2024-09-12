# conditional expressions: One line short cut of the if-else statment (ternary operator)
# syntax: condition ? value_if_true : value_if_false
# print or assign one of two values based on a condition
# x if (condition) else y

num = 5
a = 6
b = 7
age = 13
temp = 20
role = "guest"

print("positive" if num>=0 else "negative")
print("Even" if num%2==0 else "Odd")
max = a if a>b else b
min = a if a<b else b
print(max)
print(min)
access = "Full access" if role =="admin" else "No Access"
print(access)