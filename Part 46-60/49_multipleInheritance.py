# inheritance = inherit from more than one parent class
#               C (A,B)
# multilevel inheritance = inherit from a parent which inherits from another parent
#                          c(B) -> B(A) -> A


class Animal:

    def __init__(self, name):
        self.name = name
            
    
    def eat(self):
        print(f"This {self.name} is Eating")
        
    def sleep(self):
        print(f"This {self.name} is Seeping")
        
class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is Fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is Hunting")
 
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

fish = Fish("Dora")
rabbit = Rabbit("Rab")
hawk = Hawk("Eye")

rabbit.flee()
rabbit.sleep()
fish.flee()
fish.hunt()
hawk.hunt()