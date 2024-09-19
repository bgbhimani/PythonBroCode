# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class student:

    class_year = 2024
    num_student = 0
    
    

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        student.num_student += 1
    
std1 = student("Bhavik",19)
std2 = student("Axit",24)

print(f"{std1.name} {std1.age}  {student.class_year}")
print(f"{std2.name} {std2.age}  {std1.class_year}")
print(student.num_student )

