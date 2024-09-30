# Inheritance = Allows a class to inherit attributes and methods from another class
# Helps with code reusability and extensibility
# class Chiled(Parent)

class Animnal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is Eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Dog(Animnal):
    def speak():
        print("Woof!!")
        
class Cat(Animnal):
    def speak():
        print("MEOW!!")

class Mouse(Animnal):
    def speak():
        print("Squeek!!")



dog = Dog("Subby")
cat = Cat("Tom")
mouse = Mouse("Mickey")
dog.speak()
print(dog.name)
print(cat.name)
print(mouse.name)
