""""""
"""
Inheritance:(Is A Relationship)
Inheritance is an OOP mechanism in which a child class acquires the properties and methods of a parent class, 
allowing code reusability and enabling the child class to extend or override the parent class behavior.
"Why do we use inheritance?"
We use inheritance mainly for code reusability, reducing code duplication,
and creating a relationship between classes based on an “is-a” relationship.

"""
"""
Types of Inheritance

There are 5 main types:

Single Inheritance -->One parent class → one child class.

      Parent
        │
        ↓
      Child
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")
Relationship:
Dog is an Animal.
Multiple Inheritance-->One child class inherits from multiple parent classes.

    Parent 1       Parent 2
       │              │
       └──────┬───────┘
              ↓
            Child
            
class Father:
    def money(self):
        print("Father's money")


class Mother:
    def property(self):
        print("Mother's property")


class Child(Father, Mother):
    pass
    
Child gets features from both Father and Mother.

Multilevel Inheritance-->Inheritance happens in multiple levels.---->Parent → Child → Grandchild

      Grandparent
           │
           ↓
         Parent
           │
           ↓
         Child

class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Puppy(Dog):
    def cry(self):
        print("Crying")
        
Puppy can access methods from both Dog and Animal.

Hierarchical Inheritance--->One parent class has multiple child classes.

             Parent
            /      \
           ↓        ↓
        Child 1   Child 2

class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Cat(Animal):
    def meow(self):
        print("Meowing")

Both Dog and Cat inherit from Animal.

Hybrid Inheritance---> Combination of two or more types of inheritance is called hybrid inheritance.

          A
         / \
        ↓   ↓
        B   C
         \ /
          ↓
          D
Here:

A → B = inheritance
A → C = hierarchical inheritance
B, C → D = multiple inheritance

class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass

"""
"""
super()
Used to access the parent class's methods or constructor.
Commonly used with inheritance.

EX:
class Dog(Animal):
    def __init__(self):
        super().__init__()
        
"""
"""
MRO (Method Resolution Order) ---> is the order in which Python searches for a method or attribute in a class and its parent classes,
especially when multiple inheritance is used.

OOP Relationships

Inheritance → “is-a” relationship
One class inherits properties and methods from another class.
Example: Dog is an Animal

Composition → “has-a” relationship
One class contains/uses an object of another class.
Example: Car has an Engine
"""

"""__________Inheritance____________"""
#
# class A:
#     x=34
#     def __init__(self,y):
#         self.y=y
# class B(A):
#     pass
# print(B.x)
# b1=B(10)
# print(b1.y)
#
#
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f'name:{self.name}')
# class cat(Animal):
#     def display(self):
#         print(f"name:{self.name}")
#         print("Animal:cat")
# class dog(Animal):
#     def display(self):
#         super().display()
#         print("Animal:dog")
# c1=cat("chiru")
# c2=cat("raju")
# c1.display()
# c2.display()
# d1=dog("light")
# d2=dog("ganesh")
# d2.display()
# d1.display()
#
# class emp:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def display(self):
#         print(self.name, self.age, self.salary, sep="\n")
# class manager(emp):
#     def __init__(self,name,age,salary,dep):
#         super().__init__(name, age, salary)
#         self.dep=dep
#     def display(self):
#         super().display()
#         print(self.dep)
# m1=manager("raju",21,700000,"cse")
# m1.display()

"""
• Create a base class Animal with a method sound(). 
Create a derived class Dog that overrides the sound() method. 
Demonstrate method overriding.
"""
#
# class Animal:
#     def sound(self):
#         print("animal makes sound ")
#
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks: Woof! Woof!")
# a = Animal()
# d = Dog()
# # print("Base class object:")
# # a.sound()
# print(Dog.mro())
# d.sound()

"""
• Create class A with method show(). 
Create class B(A) that overrides show() and also calls the parent method using super().
"""

# class A:
#     def show(self):
#         print("hello")
# class B(A):
#     def show(self):
#         super().show()
#         print("hii")
# a1=A()
# b1=B()
#
# b1.show()

"""
• Create multi-level inheritance with classes A → B → C, 
each having a method display() printing the class name. 
Create object of C and call display(),
 showing method resolution.
"""

# class A:
#     def display(self):
#         print("class A")
# class B(A):
#     def display(self):
#         super().display()
#         print("Class B")
# class C(B):
#     def display(self):
#         super().display()
#         print("class C")
# c=C()
# c.display()

"""
• Implement hierarchical inheritance using a base class Vehicle and two child classes Car and Bike, 
each defining a method wheels().
"""
# class Vehicle:
#     def display(self):
#         print("This is Vehicle class")
# class Car(Vehicle):
#     def weels(self):
#         super().display()
#         print("car has 4 wheels")
# class Bike(Vehicle):
#     def wheels(self):
#         super().display()
#         print("bike has 2 wheels")
# c= Car()
# c.weels()
#
# b=Bike()
# b.wheels()

"""
• Create class Employee with an instance method salary(). 
Create class Manager(Employee) that overrides salary() and adds an incentive. 
Demonstrate both outputs.
"""
# class Employee:
#     def salary(self):
#         print("Employee Salary: ₹30,000")
#
#
# class Manager(Employee):
#     def salary(self):
#         print("Manager Salary: ₹50,000")
#         print("Manager Incentive: ₹10,000")
#
# emp = Employee()
# manager = Manager()
#
# emp.salary()
# manager.salary()

"""
• Create class University with a class variable and a class method. 
Inherit it into class College and access the parent’s class variable from the child class.
"""
# class University:
#     university_name = "Andhra University"   # Class variable
#
#     @classmethod
#     def show_university(cls):
#         print("University:", cls.university_name)
#
#
# class College(University):
#     pass
# print("College University:", College.university_name)
# College.show_university()

"""
Create class MathOps with a static method add(a, b). 
Create class AdvancedOps(MathOps) and use the static method without overriding it.
"""
# class Mathops:
#     @staticmethod
#     def add(a,b):
#         print(a+b)
# class Advmath(Mathops):
#     pass
# a=Advmath()
# a.add(12,14)

"""
• Create an abstract class Shape with an abstract method area().
Create class Rectangle(Shape) that implements the area() method.
"""
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#
# r = Rectangle(10, 5)
#
# print("Area:", r.area())


"""
• Create class Person with a constructor __init__(name). 
Create class Student(Person) with constructor __init__(name, roll).
 Use super() to call the parent constructor.
"""
# class Person:
#     def __init__(self,name):
#         self.name=name
# class Student(Person):
#     def __init__(self,roll,name):
#         super().__init__(name)
#         self.roll=roll
#     def display(self):
#         print("name is:",self.name)
#         print("Roll no is :",self.roll)
# c1=Student(22,"raju")
# c1.display()
"""
______________composition______________
"""
# class Light:
#     def __init__(self,brand):
#         self.brand=brand
#     def __str__(self):
#         return self.brand
# class Fan:
#     def __init__(self,fbrand):
#         self.fbrand=fbrand
#     def __str__(self):
#         return self.fbrand
# class House:
#     def __init__(self,l,f):
#         self.l=l
#         self.f=f
#     def display(self):
#         print(self.l,self.f)
# class mansion(House):
#     def __init__(self,l,f,area):
#         super().__init__(l,f)
#         self.area=area
#     def display(self):
#         super().display()
#         print(self.area)
# m=mansion(Light("phillips"),Fan('usha'),1500)
# m.display()




"""
**1. Bank Management System**

Create a Bank class with:

* balance variable
* deposit()
* withdraw()
* check_balance()

Create a User class that inherits Bank and displays the user's name. Perform deposit, withdrawal, and balance check."""
#
# class Bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#         else:
#             print("amount must greater than 0")
#     def withdraw(self,amount):
#         if amount<0:
#             print("amount must greater than 0")
#         elif amount<=self.balance:
#             self.balance-=amount
#         else:
#             print("In sufficient balance")
#     def check_balance(self):
#         print(self.balance)
# class User(Bank):
#     def __init__(self,name,balance):
#         super().__init__(balance)
#         self.name=name
# u1=User("Raju",1000)
# print("before deposite")
# u1.check_balance()
# u1.deposit(5000)
# print("after deposite")
# u1.check_balance()
# print("before withdraw")
# u1.check_balance()
# u1.withdraw(2000)
# print("after withdraw")
# u1.check_balance()
"""
**2. Employee Salary System**

Create an Employee class with:

* emp_name
* salary
* display_details()

Create a Manager class that inherits Employee and adds a bonus(). Display the total salary.
"""

# class Employee:
#     def __init__(self,emp_name,salary):
#         self.emp_name=emp_name
#         self.salary=salary
#
#     def display_details(self):
#         print(self.emp_name)
#         print(self.salary)
# class Manager(Employee):
#     def __init__(self,emp_name,salary):
#         super().__init__(emp_name, salary)
#     def bonus(self,amount):
#         self.salary+=amount
#         print("after bonus adding")
#         print(self.salary)
# m1=Manager("RAJU",50000)
# m1.display_details()
# m1.bonus(2000)


"""**3. Student Result System**

Create a Student class with:

* Name
* marks
* display_marks()

Create a Result class that inherits Student and calculates whether the student has passed or failed. """

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#
#     def display_marks(self):
#         print(self.name)
#         print(self.marks)
# class Result(Student):
#     def __init__(self,name,marks):
#         super().__init__(name, marks)
#     def displa_result(self):
#         if self.marks>=35:
#             print("pass")
#         else:
#             print("fail")
# r1=Result("Raju",95)
# r1.display_marks()
# r1 .displa_result()

"""### 4. Food Ordering System Using Multilevel Inheritance

**Class 1: Restaurant**

* Create a method menu(item) that returns the price of the selected food item.

**Class 2: FoodCourt (inherits Restaurant)**

Create the following methods:

* display_menu() – Display the available food items.
* order() – Accept the food item from the user and allow multiple orders.
* billing() – Display the total bill and add a packing charge of ₹20.

**Class 3: Customer (inherits FoodCourt)**

* Create an object of the Customer class.
* Call the order() method. 

---"""

"""### 5. Movie Ticket Booking System Using Multilevel Inheritance

**Class 1: Movie**

* Create a method ticket(movie) that returns the ticket price.

**Class 2: Booking (inherits Movie)**

Create the following methods:

* movies() – Display the available movies.
* selection() – Allow the user to book multiple tickets.
* billing() – Display the total amount and add a booking charge of ₹30.

**Class 3: Customer (inherits Booking)**

* Create an object and call the selection() method. 

---
"""
"""### 6. Online Course Enrollment System Using Multilevel Inheritance

**Class 1: Course**

* Create a method fee(course) that returns the course fee.

**Class 2: Academy (inherits Course)**

Create the following methods:

* courses() – Display available courses.
* enroll() – Allow the user to enroll in multiple courses.
* billing() – Display the total fee and add a registration fee of ₹100.

**Class 3: Student (inherits Academy)**

* Create an object and call the enroll() method. 

---"""

"""### 7. Cab Booking System Using Hierarchical Inheritance

**Class 1: Cab**

* Create methods to calculate the fare for Bike, Auto, and Car rides.

**Class 2: Uber (inherits Cab)**

* Create the methods menu(), booking(), and billing().
* Add 10% GST and apply a 15% discount if the bill is above ₹1000.

**Class 3: Ola (inherits Cab)**

* Create the methods menu(), booking(), and billing().
* Add 12% GST and apply a 20% discount if the bill is above ₹1500.

**Driver Code**

* Ask the user to choose Uber or Ola and call the booking() method. 

---"""

"""### 8. Grocery Shopping System Using Hierarchical Inheritance

**Class 1: Grocery**

* Create methods to return the price of Rice, Sugar, and Oil.

**Class 2: Dmart (inherits Grocery)**

* Create the methods items(), shopping(), and billing().
* Add 5% GST and apply a 10% discount if the bill is above ₹2000.

**Class 3: Reliance Smart (inherits Grocery)**

* Create the methods items(), shopping(), and billing().
* Add 5% GST and apply a 15% discount if the bill is above ₹2500.

**Driver Code**

* Ask the user to choose the supermarket and call the shopping() method. 

---"""
"""
### 9. Bus Ticket Booking System Using Hierarchical Inheritance

**Class 1: Bus**

* Create methods to return the fare for Sleeper, Semi-Sleeper, and AC buses.

**Class 2: RedBus (inherits Bus)**

* Create the methods routes(), booking(), and billing().
* Add 10% GST and a reservation charge of ₹30.

**Class 3: AbhiBus (inherits Bus)**

* Create the methods routes(), booking(), and billing().
* Add 10% GST and a reservation charge of ₹20.

**Driver Code**

* Ask the user to choose the platform and call the booking() method. 

---"""

"""### 10. ATM System Using Multiple Inheritance

**Class 1: SBI**

* Create the methods deposit(amount) and check_balance().

**Class 2: UnionBank**

* Create the methods withdraw(amount) and mini_statement().

**Class 3: ATM (inherits SBI and UnionBank)**

* Create the methods menu() and transaction().
* Allow the user to perform banking operations.

**Driver Code**

* Create an object of the ATM class.
* Call the transaction() method. 

---"""
"""
### 11. Paytm Application Using Multiple Inheritance

Write a Python program to implement a Paytm Application using multiple inheritance.

**Class 1: MobileRecharge**

* Create the methods recharge_plans() and mobile_recharge().

**Class 2: BusTicketBooking**

* Create the methods display_buses() and book_ticket().

**Class 3: ElectricityBills**

* Create the methods bill_details() and pay_bill().

**Class 4: Paytm (inherits MobileRecharge, BusTicketBooking, and ElectricityBills)**

Create the following methods:

* menu() – Display the available services.
* services() – Allow the user to choose and use any service (Mobile Recharge, Bus Ticket Booking, or Electricity Bill Payment). 
"""
