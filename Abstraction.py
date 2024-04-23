from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod    
    def move(self):
        pass  # Abstract method


class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving"


class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying"


# Creating objects
car = Car("Toyota")
plane = Plane("Boeing")

# Using abstraction
print(car.name)  # Output: Toyota is driving
print(plane.name)  # Output: Boeing is flying
