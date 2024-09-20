# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2. except, 3. finally

try:
    number = int(input("Enter the number: "))
    print(1/number)
# except ZeroDivisionError:
#     print("You can't divided by zero!! Man")
# except ValueError:
#     print("Enter Only Integer Values Plz")
except Exception: # it cover all exception but it's bad habit
    print("Enter Valid input")
finally:
    print("Do some clean up!!")