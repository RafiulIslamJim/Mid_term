class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute

    def get_m(self):  # Getter method
        return self.__make

    def set_mo(self, model):  # Setter method
        self.__model = model
    def get_mo(self):
        return self.__model

    def display_info(self):
        print(f"Make: {self.__make}, Model: {self.__model}")


# Creating an object
car = Car("Toyota", "Camry")

# Accessing private attributes through methods
print(car._Car__model)  # Output: Toyota
car.set_mo('jim')
print(car.get_mo())

# Trying to access private attribute directly (will raise an error)
# print(car.__make)
