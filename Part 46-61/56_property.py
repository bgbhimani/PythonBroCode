# property = Decorator used to Idefine a method as a property (it can be accessed like an attribute)
#            Benefit: Add additional logic when read, write, or delete attributes
#            Gives you getter, setter, and deleter method


class Rectangle:
    def __init__(self,width,height):
        self._height = height  # _ is for private variable
        self._width  = width

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter  # we can change the value with setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            return "Width must be greater than 0"

    @ height.setter
    def height(self,new_height):
        if new_height >0:
            self._height = new_height
        else:
            return "Width must be greater than 0"

    @ width.deleter
    def width(self):
        del self._width
        print("Width had been deleted")

    @ height.deleter
    def height(self):
        del self._height
        print("height had been deleted")

rectangle = Rectangle(5,4)

rectangle.height = 25
rectangle.width = 95

del rectangle.height
del rectangle.width

print(rectangle.width)
print(rectangle.height)