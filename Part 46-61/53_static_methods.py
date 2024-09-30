# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods   = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self,name,position) -> None:
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name}  = {self.position}"
    
    @staticmethod  # there no need to add the args in constructre is use wo that
    # we don't need to use the object of that class like here we use with directe with Employee cls
    def is_valid_position(position):
        valid_positions = ["Manager", "Cook", "Casier", "Janitor"]
        return position in valid_positions


employee1 = Employee("Bhavik" , "Manager")
employee2 = Employee("AGB" , "Casier")
employee3 = Employee("Dhruv" , "Cook")
 
print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())