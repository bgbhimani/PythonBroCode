# logical operators: evaluate multiple conditions (or,and,not)

temp = 25
is_sunny = False

if temp>25 and is_sunny:
    print("It's a beautiful day!")
elif temp<25 and not is_sunny:
    print("Don't Do Outside")
else:
    print("It's a normal day")
