# Superhero Inheritance Demo

This project demonstrates **object-oriented programming (OOP)** concepts in Python, focusing on **inheritance**, **polymorphism**, and **encapsulation** using superhero classes.

## Features

- **Base Class:** `Hero` defines core attributes and behaviors for all superheroes.
- **Inheritance:** Subclasses extend the base class with specialized properties and methods.
  - `FlyingSuperhero`: Adds flying abilities.
  - `TechSuperhero`: Adds technology gadgets.
- **Polymorphism:** Subclasses override or extend base methods to provide unique behaviors.
- **Encapsulation:** Class attributes are managed within constructors and methods.

## Example Classes

```python
class Hero(object):  
    def __init__(self, name, superpower):
        self.name = name
        self.superpower = superpower

    def introduce(self):
        return f"{self.name} has the superpower of {self.superpower}!"

class FlyingSuperhero(Hero):
    def __init__(self, name, superpower):
        super().__init__(name, superpower)
        self.flying_speed = 500

    def fly(self):
        return f"{self.name} is flying at {self.flying_speed} miles per hour!"

class TechSuperhero(Hero):
    def __init__(self, name, superpower):
        super().__init__(name, superpower)
        self.tech_gadgets = ["Gadget1", "Gadget2"]

    def use_gadget(self, gadget_name):
        if gadget_name in self.tech_gadgets:
            return f"{self.name} is using {gadget_name}!"
        else:
            return f"{self.name} doesn't have a gadget called {gadget_name}."
```

## Usage

```python
iron_man = TechSuperhero("Iron Man", "Enhanced Strength and Intelligence")
superman = FlyingSuperhero("Superman", "Flight and Super Strength")

print(iron_man.introduce())          # "Iron Man has the superpower of Enhanced Strength and Intelligence!"
print(iron_man.use_gadget("Gadget1"))# "Iron Man is using Gadget1!"
print(superman.introduce())          # "Superman has the superpower of Flight and Super Strength!"
print(superman.fly())                # "Superman is flying at 500 miles per hour!"
```

## How It Works

- **Create a base class:** All superheroes inherit from `Hero`.
- **Extend functionality:** Subclasses like `FlyingSuperhero` and `TechSuperhero` have custom methods and attributes.
- **Instantiate and use:** Create superhero objects and call their methods to see OOP principles in action.

## Getting Started

1. Copy the example classes into your Python file.
2. Create your own superhero subclasses to practice inheritance and polymorphism.
3. Run the usage example to see output demonstrating OOP concepts.

## License

This project is for educational purposes.

---

