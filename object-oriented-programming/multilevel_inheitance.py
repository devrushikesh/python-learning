
 # here is the multilevel inheritance 
#  inherit from a parent which inherits from another parent
#  C(B) <- B(A) <- A

class Animal:
    def eat(self):
        print("This animal is eating")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator): 
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()


rabbit.flee()
rabbit.eat()
# rabbit.hunt() --> gives error bacause this animal is not predator



hawk.hunt()
hawk.eat()
# hawk.flee()  --> gives error because this animal is not Prey

# No error in fish because this animal can  be both like Prey and Predator
fish.flee()
fish.eat()
fish.hunt()
