# Polymorphism = Greek word that means to "have many forms or faces"
#       Poly   = Many
#       Morphe = Form
#
#       TWO WAYS TO ACHIEVE POLYMORPHISM
#       1. Inheritance    = An object could be treated of the same type as a parent class
#       2. "Duck typing"  = Object must have necessary attributes/methods

#1.Inheritance:

from abc import ABC, abstractclassmethod



class Shape:
    
    @abstractclassmethod
    def area(self):
        pass

class Circle(Shape):
        def __init__(self,radius) -> None:
            self.radius = radius
            
        def area(self):
            return 3.14*2*self.radius

class Square(Shape):
    def __init__(self,width) -> None:
        self.width = width
    def area(self):
        return self.width**2

class Triangle(Shape):
    def __init__(self,height,width) -> None:
        self.width = width
        self.height = height
        
    def area(self):
        return 0.5*self.width*self.height

class Pizza(Circle):
    def __init__(self, radius,toppings) -> None:
        super().__init__(radius)
        self.toppings = toppings

    
shapes = [Circle(8),Square(2),Triangle(2,2),Pizza(15,"pepproni")]

for shap in shapes:
    print(f"{shap.area()} cm²")