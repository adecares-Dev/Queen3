#  Base class to demonstrate inheritance
class Hero(object):  
    def __init__(self, name, superpower):
        self.name = name
        self.superpower = superpower

    def introduce(self):
        return f"{self.name} has the superpower of {self.superpower}!"


class FlyingSuperhero(Hero):  # Inheritance layer, showing polymorphism
    def __init__(self, name, superpower):
        super().__init__(name, superpower)
        self.flying_speed = 500  # Attribute to add more detail

    def fly(self):
        return f"{self.name} is flying at {self.flying_speed} miles per hour!"


class TechSuperhero(Hero):  # Another inheritance layer, showing different attributes
    def __init__(self, name, superpower):
        super().__init__(name, superpower)
        self.tech_gadgets = ["Gadget1", "Gadget2"]  # Collection of tech gadgets

    def use_gadget(self, gadget_name):
        if gadget_name in self.tech_gadgets:
            return f"{self.name} is using {gadget_name}!"
        else:
            return f"{self.name} doesn't have a gadget called {gadget_name}."


# Instantiating objects with unique values
iron_man = TechSuperhero("Iron Man", "Enhanced Strength and Intelligence")
superman = FlyingSuperhero("Superman", "Flight and Super Strength")

# Demonstrating polymorphism and encapsulation
print(iron_man.introduce())  # Using superclass method
print(iron_man.use_gadget("Gadget1"))  # Using subclass method
print(superman.introduce())  # Using superclass method
print(superman.fly())  # Using subclass method





