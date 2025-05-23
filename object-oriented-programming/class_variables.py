'''
 class variables = Shared among all instances of a class
                   Defined outside the constructor
                   Allow you to share data among all objects created from the class

'''



class Student:
    class_year = 2025
    student_count = 0 # class vairable

    def __init__(self, name, age):
        self.name = name # self.name is a instance variable
        self.age = age
        Student.student_count += 1



std1 = Student("Rushikesh Choudhari", 23)
std2 = Student("Kunal Jaiswal", 25)

print(std1.name)
print(std1.age)
print(std1.class_year)



print(std2.name)
print(std2.age)
print(std2.class_year) 

# class variables can be accessible via object of the class and the Class name it self also


print(Student.student_count)