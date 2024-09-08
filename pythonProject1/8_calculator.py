choice = input("Enter your choice (+,-,*,/): ")
a = float(input("Enter the number1 :"))
b = float(input("Enter the number2 :"))

if choice == "+":
    print(a+b)
elif choice == "-":
    print(a-b)
elif choice == "*":
    print(a*b)
elif choice == "/":
    print(a/b)
else:
    print("Enter Valid Choice")