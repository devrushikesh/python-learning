
'''

Polymorphism is a foundational concept in programming that allows entities like functions, methods or operators to behave 
differently based on the type of data they are handling. Derived from Greek, the term literally means "many forms".

Python's dynamic typing and duck typing make it inherently polymorphic. Functions, operators and even built-in objects like
loops exhibit polymorphic behavior.

'''


class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement 'move'")

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"
    
    def honk(self):
        return "Honk! Honk!"

class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on water"
    
    def anchor(self):
        return "Dropping anchor!"

class Airplane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"
    
    def takeoff(self):
        return "Cleared for takeoff!"

# --------------- Polymorphism in Action ---------------
def travel(vehicle):
    print(vehicle.move())

# Create objects
car = Car()
boat = Boat()
plane = Airplane()

# Same function works for ALL vehicles
travel(car)    # Output: 🚗 Driving on the road
travel(boat)   # Output: ⛵ Sailing on water
travel(plane)  # Output: ✈️ Flying in the sky

# --------------- Bonus: Duck Typing Example ---------------
class Bicycle:
    # Not a subclass of Vehicle, but has 'move()'
    def move(self):
        return "🚲 Pedaling on the cycle path"

# Works even though Bicycle isn't a Vehicle subclass!
travel(Bicycle())  # Output: 🚲 Pedaling on the cycle path