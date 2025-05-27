"""
 Static Methods  = A static method is a method bound to the class (not the instance) that doesn't access 
                   self or cls. It's defined using @staticmethod and behaves like a regular function but 
                   belongs to the class's namespace.
"""



class Student:
    class_year = 2025
    student_count = 0 # class vairable or static variables

    def __init__(self, name, age):
        self.name = name # self.name is a instance variable
        self.age = age
        Student.student_count += 1

    @staticmethod
    def increment_class_year():
        Student.class_year += 1



std1 = Student("Rushikesh Choudhari", 23)
std2 = Student("Kunal Jaiswal", 25)

print(std1.name)
print(std1.age)
print(std1.class_year)



print(std2.name)
print(std2.age)
print(std2.class_year) 

# class variables can be accessible via object of the class and the Class name it self also

Student.increment_class_year() # no need to create the obj for calling the static methods using class names

print("updated class year ",Student.class_year)
