""""""
"""
Abstraction -> Hide the unnecessary implementation details and show only what the user needs to use.

"""

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
