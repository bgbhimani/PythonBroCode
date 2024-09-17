# print(__name__)  # __main__
# from script2 import *

def favoritefood(food):
    print(f"My favorite food is {food}")

def main():
    print("This is Script 1")
    favoritefood("Dhosa")
    print("Good Bye")
    
if __name__ == '__main__':
    main()
# if this code is not there than whenever import it will show that code
