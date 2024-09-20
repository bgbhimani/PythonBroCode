# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

class Student:
    count = 0
    total_gpa = 0
    
    def __init__(self,name,gpa) -> None:
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    # Intance Method
    def get_info(self):
        return f"{self.name}  = {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total Students : {cls.count}"
    
    @classmethod
    def get_total_gpa(cls):
        return f"Total GPA : {cls.total_gpa:.2f}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA : {cls.total_gpa/cls.count  :.2f}"

std1 = Student("Bhavik",8.21)
std2 = Student("AGB",8.10)
print(std1.get_info())

print(Student.get_count())
print(Student.get_total_gpa())
print(Student.get_avg_gpa())