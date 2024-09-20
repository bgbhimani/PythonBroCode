# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methods
#                "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(Self):
        print("Woof!")

class Cat(Animal):
    def speak(Self):
        print("Meow!")
        
class Car:
    alive = False
    def speak(self):
        print("Horn!")
        
        
animals = [Dog(),Cat(),Car()]


for animal in animals:
    animal.speak()
    print(f"{'Alive' if animal.alive else 'Not Alive'}")