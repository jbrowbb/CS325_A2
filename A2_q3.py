from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == "__main__":

    circle = Circle(5)
    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())

    rectangle = Rectangle(4,6)
    print("Rectangle Area:", rectangle.area())
    print("Rectangle Perimeter:",rectangle.perimeter())