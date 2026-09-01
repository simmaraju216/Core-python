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
class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)
    def __eq__(self, other):
        return self.a==other.a and self.b==other.b
    def __str__(self):
        return f"{self.a},{self.b}"

v1=Vector(12,14)
v2=Vector(15,20)
print(v1+v2)
print(v1==v2)

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