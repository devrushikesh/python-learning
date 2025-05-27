# ENCAPSULATION IN PYTHON
# ======================
# Encapsulation is the concept of bundling data (variables) and methods (functions) 
# that operate on the data into a single unit (class). It also restricts direct access 
# to some of the object's components, which is known as data hiding.

class Employee:
    def __init__(self):
        # Private variable (using double underscore __)
        # This variable cannot be accessed directly from outside the class.
        self.__salary = 50000  

    # Getter method (allows controlled access to private variable)
    def get_salary(self):
        """Returns the employee's salary (private data)."""
        return self.__salary

    # Setter method (allows controlled modification of private variable)
    def set_salary(self, new_salary):
        """Sets a new salary only if it's valid (positive value)."""
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Error: Salary must be positive!")

# ===== USING THE CLASS =====
emp = Employee()

# Trying to access __salary directly (Won't work due to encapsulation)
# print(emp.__salary)  # Error: AttributeError (private variable)

# Correct way: Using getter and setter methods
print("Current Salary:", emp.get_salary())  # Output: 50000
emp.set_salary(60000)  # Updates salary
print("Updated Salary:", emp.get_salary())  # Output: 60000

emp.set_salary(-1000)  # Output: "Error: Salary must be positive!"