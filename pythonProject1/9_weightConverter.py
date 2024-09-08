w = float(input("Enter Your Wieght:" ))
u = input("Enter the Unit(lbs/kg): ")

if u == "lbs":
    w = 0.4535*w
    print(f"your wight in kg is: {round(w,2)}")
elif u == "kg":
    w = w*2.204623
    print(f"your wight in lbs is: {round(w,2)}")
else:
    print("Enter the Valid Number")