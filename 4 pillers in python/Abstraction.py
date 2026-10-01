""""""
"""
Abstraction -> Hide the unnecessary implementation details and show only what the user needs to use.

1. Abstraction

Abstraction is an OOP concept where we hide unnecessary implementation details and show only the essential features.

Example:
When you use an ATM, you select Withdraw, but you don't need to know the internal banking code that processes the withdrawal.

2. Abstract Method

An abstract method is a method that is declared but does not have an implementation in the abstract class. 
The child class must provide its implementation.
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts with a key")


car = Car()
car.start()
"""--------------------------------------"""
class Car:
    def start(self):
        self.__check_engine()
        self.__inject_fuel()
        self.__ignite()

        print("Car started")

    def __check_engine(self):
        print("Checking engine")

    def __inject_fuel(self):
        print("Injecting fuel")

    def __ignite(self):
        print("Igniting engine")
car = Car()
car.start()


"""
11. Using abc module: 
• Create an abstract class Shape with area(), perimeter() 
• Implement Circle, Rectangle, Triangle Demonstrate: 
• why base class should NOT contain calculation logic 
• what happens if a subclass fails to implement one of the methods 
"""

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

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# Objects
circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(3, 4, 5)

print("Circle")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

print("\nRectangle")
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

print("\nTriangle")
print("Area:", triangle.area())
print("Perimeter:", triangle.perimeter())