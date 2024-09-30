# suppr() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods
import math
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
        
    def describe(self):
        print(f"It is {self.color} and { 'filled' if self.filled else 'not filled' }")
    
class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius = radius
        
    def describe(self):
        super().describe()
        print(f"It is the Circle with The Area: {(2* math.pi*self.radius):.2f}")
        
class Square(Shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width = width
    
    def describe(self):
        super().describe()
        print(f"It is the Square with The Area: {(self.width**2):.2f}")

class Triangle(Shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.width = width
        self.height = height
        
    def describe(self):
        super().describe()
        print(f"It is the Circle with The Area: {(0.5 * self.height * self.width):.2f}")
        
circle = Circle("Blue",True,5)
square = Square("Red",False,6)
triangle = Triangle("Yellow",True,6,7)


print(f"{circle.color}  {circle.filled}  {circle.radius}")
print(f"{square.color}  {square.filled}  {square.width}Cm")
print(f"{triangle.color} {triangle.filled} {triangle.height}cm  {triangle.width}cm")

circle.describe()
square.describe()
triangle.describe()