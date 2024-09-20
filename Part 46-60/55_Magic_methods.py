# Magic methods = Dunder methods (double underscore)  __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects
# it is runn back the code
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    # return the string represtion of the Object
    def __str__(self) -> str:  
        return f"'{self.title}' By {self.author}"
    
    def __eq__ (self,other):
        return self.title == other.title and self.author == other.author
    
    def __lt__ (self,other):
        return  self.num_pages < other.num_pages

    def __gt__ (self,other):
        return  self.num_pages > other.num_pages
    
    def __add__ (self,other):
        return  self.num_pages + other.num_pages
    
    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, item):
        if item == 'title':
            return self.title
        elif item == 'author':
            return self.author
        elif item == "num_pages":
            return self.num_pages
        else:
            return f"'{item}' key not found"


book1 = Book("The Hobbit","JRR Tolking",500)
book2 = Book("Harry Potter","JK Roling",526)
book3 = Book("The Lion King" ,"Don't know", 321)
book4 = Book("The Lion King" ,"Don't know", 321)

print(book1 == book2)   # False
print(book3 == book4)   # True
print(book2 < book3)   # False
print(book2 > book3)   # True if there's not magic method it shows the error
print(book2+book3)   #847
print("Harry" in book2)  # True
print(book1['title'])
print(book3['num_pages'])
