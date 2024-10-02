t = float(input("Enter The Temperature: "))

u = input("Enter the unit (c/f) ")

if u == "c":
    f = (t * 9/5) + 32
    print(f"The temperature in Fahrenheit is {round(f,2)}")
elif u == "f":
    c = (t - 32) * 5/9
    print(f"The temperature in Celsius is {round(c)}")
else:
    print("Invalid unit")