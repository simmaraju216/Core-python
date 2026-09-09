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
