

class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):  # here is the multiple inheritance 
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()



rabbit.flee()
# rabbit.hunt() --> gives error bacause this animal is not predator

hawk.hunt()
# hawk.flee()  --> gives error because this animal is not Prey

# No error in fish because this animal can  be both like Prey and Predator
fish.flee()
fish.hunt()

