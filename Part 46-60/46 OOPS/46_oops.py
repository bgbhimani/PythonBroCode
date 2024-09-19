# Object = A "bundle" of related attributes (variables) and me Ods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object


from car import Car
    
car1 = Car("Mustang",2024,"Blue",False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()
car1.stop()
car1.describe()
print()

car2  =Car("Audi",2021,"Red",True)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
