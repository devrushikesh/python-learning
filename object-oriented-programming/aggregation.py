class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Aggregation: Car has an Engine

    def start_car(self):
        return f"{self.brand} car: {self.engine.start()} with {self.engine.horsepower} HP"

# Create an Engine object
engine = Engine(150)

# Pass the Engine object to the Car
car = Car("Toyota", engine)

# Start the car
print(car.start_car())