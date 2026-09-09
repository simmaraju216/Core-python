"""
Polymorphism
"""
"""
Polymorphism is one of the four main principles of Object-Oriented Programming (OOP). 
The word Polymorphism comes from Greek:

Poly = Many
Morph = Forms

1)Compile time polymorphism --->Method overloading
2)Run time --->Method overraiding
3)Duck Typing
"""
"""
1)Compile time polymorphism --->Method overloading
Python does not support traditional method overloading.like c++,java

"Does Python support method overloading?"

A good answer is:

Python does not support traditional method overloading like Java or C++. 
If we define multiple methods with the same name, the latest definition replaces the previous one.
 However, we can achieve overloading-like behavior using default arguments, *args, **kwargs
"""
# class Calculator:
#
#     def add(self, a, b):   #Because Python is dynamically typed, and method definitions are stored by name.
#         return a + b       # for the second time, it replaces the first definition.
#
#     def add(self, a, b, c):
#         return a + b + c
# obj = Calculator()
#
# print(obj.add(10, 20))

"""
But We can achieve overloading-like behavior using:
Default peremeters
*args
**kargs
"""
class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c

obj = Calculator()

print(obj.add(10))
print(obj.add(10, 20))
print(obj.add(10, 20, 30))
# using * args
class Calculator:

    def add(self, *args):
        return sum(args)

obj = Calculator()

print(obj.add(10, 20))
print(obj.add(10, 20, 30))
print(obj.add(1, 2, 3, 4, 5))

"""
2)Run time --->Method overriding
Method overriding occurs when a child class provides its own implementation
 of a method that is already defined in the parent class.
 
 
 It is called runtime polymorphism because Python decides which method to execute at runtime, 
 based on the actual object.
"""
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()

"""
3)Duck Typing
Duck Typing is one of the most important concepts in Python polymorphism.

"If it walks like a duck and quacks like a duck, then it is a duck."


Python cares about what an object can do, rather than what type the object is.

Duck typing does not require inheritance.
"""
class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
"""
"I don't care whether you're a Dog or Cat. If you can perform sound(), I'll use you."
That's Duck Typing.
"""

"""
4)Operator Overloading
"""
print(5 + 3)

"""
using polymorphism we can change the behaviour of Operator

You can overload operators using special (magic) methods.
is called custom Operator Overloading
"""
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student(90)
s2 = Student(80)

print(s1 + s2)



"""_____________questions_________________"""
"""
Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that override it. 
Demonstrate polymorphism by iterating over a list of different animal objects and calling make_sound(). 
"""
class Animal:
    def make_sound(self):
        print("animal make sound")
class Dog(Animal):
    def make_sound(self):
        print("BOWWWW")
class Cat(Animal):
    def make_sound(self):
        print("MEWWWW")
class Cow(Animal):
    def make_sound(self):
        print("AMBAAAAA")
a=Animal()
d=Dog()
c=Cat()
cw=Cow()

a.make_sound()
d.make_sound()
c.make_sound()
cw.make_sound()

"""
Q2. Write a function operate(device) that calls device.start(). 
Pass in objects of Car, Computer, and WashingMachine — all of which define a start() method, but share no inheritance relationship. 
Show that Python’s polymorphism works through behavior, not type. 
"""
class Car:
    def start(self):
        print("car is started")
class Computer:
    def start(self):
        print("computer is started")
class WashingMachine :
    def start(self):
        print("washing machine is started")
def operate(device):
    device.start()
operate(Car())
operate(Computer())
operate(WashingMachine())


"""
 Create a Vector class that supports: 
 • + operator → add coordinates 
 • == operator → compare equality 
 Show how operator overloading gives natural polymorphism to user-defined classes. 
"""
# class Vector:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self, other):
#         return Vector(self.a+other.a,self.b+other.b)
#     def __eq__(self, other):
#         return self.a==other.a and self.b==other.b
#     def __str__(self):
#         return f"{self.a},{self.b}"
#
# v1=Vector(12,14)
# v2=Vector(15,20)
# print(v1+v2)
# print(v1==v2)

"""
Q4. Create a base class Transport with move()
and derived classes Bus and Bike that override it but also call the parent implementation using super(). 
Show the combination of reuse + custom behavior. 
"""
class Transport:
    def move(self):
        print("vechicle is moving")
class Bus(Transport):
    def move(self):
        super().move()
        print("move by bus")
class Bike(Transport):
    def move(self):
        super().move()
        print("move by bike")
b1=Bus()
b2=Bike()
b1.move()
b2.move()

"""
Q5. Using the abc module, create an abstract class Notification with send(). 
Implement subclasses EmailNotification, SMSNotification, PushNotification — each with its own send() logic.
Demonstrate polymorphism by looping over all and calling send(). 
"""
from abc import ABC, abstractmethod
class Notification(ABC):
    @ abstractmethod
    def send(self):
        pass
class EmailNotification(Notification):
    def send(self):
        print("Sending notification via Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending notification via SMS")
class PushNotification(Notification):
    def send(self):
        print("Sending notification via Push Notification")

notifications = [EmailNotification(),SMSNotification(),PushNotification()]
for i in notifications:
    i.send()


"""
Q6. Design: • Base class Payment with process(amount) 
•Subclass CreditCardPayment adds process(amount, card_type)
Demonstrate what happens when overriding with different signatures and how Python handles it. 
"""
class Payment:
    def process(self, amount):
        print(f"Processing payment of ₹{amount}")


class CreditCardPayment(Payment):
    # Overriding process() with an additional parameter
    def process(self, amount, card_type):
        print(f"Processing ₹{amount} using {card_type} credit card")

# Base class object
p1 = Payment()
p1.process(500)

# Subclass object
p2 = CreditCardPayment()
p2.process(1000, "Visa")

"""
*****
Q7. Create: 
• Class Sorter with change(strategy) method.
Separate strategy classes: BS, MS, QS, each implementing a different logic method.
Demonstrate how polymorphism can be achieved without inheritance by using interchangeable strategy objects. 
"""
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def change(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)


# Bubble Sort strategy
class BS:
    def sort(self, data):
        arr = data.copy()

        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr


# Merge Sort strategy
class MS:
    def sort(self, data):
        if len(data) <= 1:
            return data.copy()

        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])

        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result


# Quick Sort strategy
class QS:
    def sort(self, data):
        if len(data) <= 1:
            return data.copy()

        pivot = data[0]

        left = [x for x in data[1:] if x <= pivot]
        right = [x for x in data[1:] if x > pivot]

        return self.sort(left) + [pivot] + self.sort(right)


# Demonstrating polymorphism
data = [5, 2, 8, 1, 9, 3]

sorter = Sorter(BS())
print("Bubble Sort:", sorter.sort(data))

sorter.change(MS())
print("Merge Sort :", sorter.sort(data))

sorter.change(QS())
print("Quick Sort :", sorter.sort(data))


"""
Q8. Create: 
• Base Account → withdraw() 
• Subclass SavingsAccount → modifies withdraw() 
• Subclass PremiumSavingsAccount → overrides again but calls parent using super() Show how polymorphism works across multiple levels. 
"""

class Account:
    def withdraw(self, amount):
        print(f"Account: Withdrawing ₹{amount}")


class SavingsAccount(Account):
    def withdraw(self, amount):
        print(f"SavingsAccount: Withdrawing ₹{amount}")
        print("Savings account withdrawal rules applied")


class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self, amount):
        print(f"PremiumSavingsAccount: Processing ₹{amount}")

        # Call the parent class method
        super().withdraw(amount)

        print("Premium benefits applied")


# Objects of different levels
accounts = [
    Account(),
    SavingsAccount(),
    PremiumSavingsAccount()
]

# Polymorphism
for account in accounts:
    account.withdraw(1000)

"""
Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and Rectangle, 
each implementing a draw() method. 
Add another unrelated class Car with draw() and pass it — what happens and why? 
"""
class Circle:
    def draw(self):
        print("Drawing a Circle")


class Square:
    def draw(self):
        print("Drawing a Square")


class Rectangle:
    def draw(self):
        print("Drawing a Rectangle")


class Car:
    def draw(self):
        print("Drawing a Car")


# Polymorphic function
def draw(shape):
    shape.draw()


# Different objects
draw(Circle())
draw(Square())
draw(Rectangle())
draw(Car())

"""
Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a pay() method. 
Now implement a version that checks types explicitly using isinstance() before calling pay(). 
Compare both designs and explain why one breaks the spirit of polymorphism. 
"""

# Payment classes
class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


class Cash:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


# -------------------------------
# Design 1: Polymorphism
# -------------------------------

def make_payment(payment_method, amount):
    payment_method.pay(amount)


print("Polymorphic design:")
make_payment(UPI(), 500)
make_payment(Card(), 1000)
make_payment(Cash(), 200)


# -------------------------------
# Design 2: Using isinstance()
# -------------------------------

def make_payment_with_check(payment_method, amount):
    if isinstance(payment_method, UPI):
        payment_method.pay(amount)

    elif isinstance(payment_method, Card):
        payment_method.pay(amount)

    elif isinstance(payment_method, Cash):
        payment_method.pay(amount)

    else:
        print("Unsupported payment method")


print("\nUsing isinstance():")
make_payment_with_check(UPI(), 500)
make_payment_with_check(Card(), 1000)
make_payment_with_check(Cash(), 200)