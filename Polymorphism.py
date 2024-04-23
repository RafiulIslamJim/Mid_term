class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Function to calculate total area of shapes
def total_area(shapes):
    total = 0
    for shap in shapes:
        total += shap.area()
    return total


# Creating objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Using polymorphism
print(rectangle.area())  # Output: Total area: 83.14
