# Variable = a container for a value. Behaves as the values that it contains

first_name = "Bhavik"
last_name = "Bhimani"
full_name = first_name + " " + last_name
print(type(full_name))       # <class 'str'>
print("Hello, " + full_name) # Bhavik


age = 18
age = age +1
print("your age is:",age)
print(type(age))    #<class 'int'>


height = 250.5
print("Your Height is " + str(height) + "cm")
print(type(height)) #<class 'float'>


human = True
print("Are yout= Human: " + str(human))
print(type(human))  #<class 'bool'>