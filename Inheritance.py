class Animal:
    def __init__(self, species):
        self.species = species

   # def speak(self):
    #    pass  # Abstract method


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


# Creating objects
dog = Dog("Canine")
cat = Cat("Feline")

# Calling methods
print(dog.species)  # Output: Canine
print(dog.speak())  # Output: Woof
print(cat.species)  # Output: Feline
print(cat.speak())  # Output: Meow
