'''
Inheritance = Allows a class to inherit attributes and methods from another class
              Helps with code reusability and extensibility
              class Child(Parent)
'''


# Create the parent class named as Animal

class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True
    

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")


# Create the child class inherit from Animal class

class Cat(Animal):
    
    def speak(self):
        print("MEOW!")

class Dog(Animal):
    
    def speak(self):
        print("WOOF!")




cat1 = Cat("Emmiy")
print(cat1.name)
print(cat1.is_alive)
cat1.eat()
cat1.speak()
cat1.sleep()



dog1 = Dog("Jack")
print(dog1.name)
print(dog1.is_alive)
dog1.eat()
dog1.speak()
dog1.sleep()