# name = input("Enter Your Name: ")
name = "bhavaiak" 
num = "91-987-985-875-1"

result = len(name)
result = name.find("ha")  # 1
result = name.rfind("a") # last char if exist
result = name.capitalize()
result  = name.upper()
result = name.lower()
# result = num.isdigit()
result = name.isalpha()
result = name.zfill(15)
result = num.count("-")
num = num.replace("-"," ")

print(result)
print(num)

print(help(str))