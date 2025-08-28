from abc import ABC, abstractmethod

# Abstract base class
class Mover(ABC):
    @abstractmethod
    def move(self):
        pass


# Vehicle subclasses
class Car(Mover):
    def move(self):
        return "Driving 🚗"


class Plane(Mover):
    def move(self):
        return "Flying ✈️"


class Boat(Mover):
    def move(self):
        return "Sailing ⛵"


# Animal subclasses
class Horse(Mover):
    def move(self):
        return "Galloping 🐎"


class Bird(Mover):
    def move(self):
        return "Soaring 🐦"


class Fish(Mover):
    def move(self):
        return "Swimming 🐟"


# List of mixed objects
movers = [Car(), Plane(), Boat(), Horse(), Bird(), Fish()]

# Demonstrate polymorphic behavior
for mover in movers:
    print(f"{type(mover).__name__} is {mover.move()}")









        
