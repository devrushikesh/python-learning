

# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects


# class = (blueprint) used to design the structure and layout of an object


# create the class with constructor
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")
    
    def stop(self):
        print(f"You Stop the {self.model}")



# create the object of the class

car1 = Car("Mustang", 2024, "black", True)
car2 = Car("BMW", 2025, "red", False)


print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()
car1.stop()



print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
car2.drive()
car2.stop()