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

"""4. Food Ordering System Using Multilevel Inheritance

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

# class Restaurant:
#     def menu(self, item):
#         food = {
#             "pizza": 200,
#             "burger": 120,
#             "biryani": 180,
#             "fries": 80,
#             "sandwich": 100
#         }
#
#         return food.get(item, 0)
#
#
# class FoodCourt(Restaurant):
#
#     def display_menu(self):
#         print("\n----- MENU -----")
#         print("Pizza    - ₹200")
#         print("Burger   - ₹120")
#         print("Biryani  - ₹180")
#         print("Fries    - ₹80")
#         print("Sandwich - ₹100")
#
#     def order(self):
#         self.total = 0
#
#         while True:
#             item = input("\nEnter food item: ").lower()
#
#             price = self.menu(item)
#
#             if price == 0:
#                 print("Item not available!")
#             else:
#                 self.total += price
#                 print(item, "added - ₹", price)
#
#             choice = input("Do you want to order more? (yes/no): ").lower()
#
#             if choice != "yes":
#                 break
#
#         self.billing()
#
#     def billing(self):
#         packing_charge = 20
#         final_bill = self.total + packing_charge
#
#         print("\n----- BILL -----")
#         print("Food Total    : ₹", self.total)
#         print("Packing Charge: ₹", packing_charge)
#         print("Total Bill    : ₹", final_bill)
#
#
# class Customer(FoodCourt):
#     pass
#
#
# customer = Customer()
#
# customer.display_menu()
#
# customer.order()

""" 5. Movie Ticket Booking System Using Multilevel Inheritance

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
# class Movie:
#     def ticket(self,movie):
#
#         movies = {
#             "avengers": 200,
#             "bahubali": 180,
#             "kgf": 150,
#             "pushpa": 160,
#             "rrr": 180
#         }
#
#         return movies.get(movie, 0)
# class Booking(Movie):
#     def movies(self):
#         print("\n----- AVAILABLE MOVIES -----")
#         print("Avengers - ₹200")
#         print("Bahubali - ₹180")
#         print("KGF     - ₹150")
#         print("Pushpa  - ₹160")
#         print("RRR     - ₹180")
#     def selection(self):
#         self.total = 0
#
#         while True:
#             movie=input().lower()
#             price=self.ticket(movie)
#             if price==0:
#                 print("Movie not available")
#             else:
#                 self.total+=price
#                 print(movie,"---₹",price)
#             choice=input("you want to book another ticket?").lower()
#
#             if choice!="yes":
#                 break
#         self.billing()
#     def billing(self):
#         booking_charge = 30
#         final_amount = self.total + booking_charge
#
#         print("\n----- BILL -----")
#         print("Ticket Amount : ₹", self.total)
#         print("Booking Charge: ₹", booking_charge)
#         print("Total Amount  : ₹", final_amount)
# class Customer(Booking):
#     pass
# customer = Customer()
#
# customer.movies()
#
# customer.selection()

"""6. Online Course Enrollment System Using Multilevel Inheritance

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
# class Course:
#     def fee(self,course):
#         courses_list={
#             "python": 500,
#             "java": 700,
#             "c": 150,
#             "c++": 300,
#             "html": 180
#         }
#         return courses_list.get(course,0)
#
# class Academy(Course):
#     def courses(self):
#         print("\n----- AVAILABLE MOVIES -----")
#         print("PYTHON - ₹500")
#         print("JAVA - ₹700")
#         print("C     - ₹150")
#         print("C++  - ₹300")
#         print("HTML     - ₹180")
#
#     def enroll(self):
#         self.total = 0
#         while True:
#             course = input().lower()
#             price = self.fee(course)
#             if price == 0:
#                 print("Course not available")
#             else:
#                 self.total += price
#                 print(course, "---₹", price)
#             choice = input("you want to enroll another course?").lower()
#
#             if choice != "yes":
#                 break
#         self.billing()
#
#     def billing(self):
#         registration_fee = 100
#         final_amount = self.total + registration_fee
#
#         print("\n----- BILL -----")
#         print("Courses Amount : ₹", self.total)
#         print("Registration Fee: ₹", registration_fee)
#         print("Total Amount  : ₹", final_amount)
#
# class Student(Academy):
#     pass
# s1=Student()
# s1.courses()
# s1.enroll()

""" 7. Cab Booking System Using Hierarchical Inheritance

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
# class Cab:
#     def bike_fare(self, km):
#         return km * 10
#
#     def auto_fare(self, km):
#         return km * 15
#
#     def car_fare(self, km):
#         return km * 20
#
# class Uber(Cab):
#     def menu(self):
#         print("\n----- UBER -----")
#         print("1. Bike - ₹10/km")
#         print("2. Auto - ₹15/km")
#         print("3. Car  - ₹20/km")
#     def booking(self):
#         self.menu()
#         choice = input("Choose ride: ")
#         km = float(input("Enter distance in km: "))
#         if choice == "1":
#             self.total = self.bike_fare(km)
#         elif choice == "2":
#             self.total = self.auto_fare(km)
#         elif choice == "3":
#             self.total = self.car_fare(km)
#         else:
#             print("Invalid choice!")
#             return
#
#         self.billing()
#     def billing(self):
#         gst = self.total * 0.10
#         amount = self.total + gst
#
#         if amount > 1000:
#             discount = amount * 0.15
#         else:
#             discount = 0
#
#         final_amount = amount - discount
#         print("\n----- UBER BILL -----")
#         print("Fare      : ₹", self.total)
#         print("GST (10%) : ₹", gst)
#         print("Discount  : ₹", discount)
#         print("Total Bill: ₹", final_amount)
#
# class Ola(Cab):
#     def menu(self):
#         print("\n----- Ola -----")
#         print("1. Bike - ₹10/km")
#         print("2. Auto - ₹15/km")
#         print("3. Car  - ₹20/km")
#     def booking(self):
#         self.menu()
#         choice = input("Choose ride: ")
#         km = float(input("Enter distance in km: "))
#         if choice == "1":
#             self.total = self.bike_fare(km)
#         elif choice == "2":
#             self.total = self.auto_fare(km)
#         elif choice == "3":
#             self.total = self.car_fare(km)
#         else:
#             print("Invalid choice!")
#             return
#
#         self.billing()
#     def billing(self):
#         gst = self.total * 0.12
#         amount = self.total + gst
#
#         if amount > 1500:
#             discount = amount * 0.20
#         else:
#             discount = 0
#
#         final_amount = amount - discount
#         print("\n----- Ola BILL -----")
#         print("Fare      : ₹", self.total)
#         print("GST (12%) : ₹", gst)
#         print("Discount  : ₹", discount)
#         print("Total Bill: ₹", final_amount)
# print("----- CAB BOOKING -----")
# print("1. Uber")
# print("2. Ola")
#
# choice = input("Choose cab: ")
#
# if choice == "1":
#     cab = Uber()
#     cab.booking()
#
# elif choice == "2":
#     cab = Ola()
#     cab.booking()
#
# else:
#     print("Invalid choice!")
""" 8. Grocery Shopping System Using Hierarchical Inheritance

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

# class Grocery:
#     def rice(self):
#         return 60
#     def sugar(self):
#         return 40
#     def oil(self):
#         return 160
# class Dmart(Grocery):
#     def items(self):
#         print("\n----- DMART ITEMS -----")
#         print("1. Rice  - ₹60/kg")
#         print("2. Sugar - ₹40/kg")
#         print("3. Oil   - ₹160/litre")
#     def shopping(self):
#         self.items()
#         self.total=0
#         while True:
#             choice=input("\nEnter item (rice/sugar/oil): ").lower()
#             quantity = int(input("Enter quantity: "))
#
#             if choice == "rice":
#                 price = self.rice()
#             elif choice == "sugar":
#                 price = self.sugar()
#             elif choice == "oil":
#                 price = self.oil()
#             else:
#                 print("Item not available!")
#                 continue
#             amount = price * quantity
#             self.total += amount
#             print("Item added: ₹", amount)
#
#             more = input("Do you want to buy more? (yes/no): ").lower()
#
#             if more != "yes":
#                 break
#         self.billing()
#
#     def billing(self):
#         gst = self.total * 0.05
#         amount = self.total + gst
#
#         if amount > 2000:
#             discount = amount * 0.10
#         else:
#             discount = 0
#
#         final_amount = amount - discount
#
#         print("\n----- DMART BILL -----")
#         print("Shopping Amount : ₹", self.total)
#         print("GST (5%)        : ₹", gst)
#         print("Discount (10%)  : ₹", discount)
#         print("Final Bill      : ₹", final_amount)
#
# class RelianceSmart(Grocery):
#
#     def items(self):
#         print("\n----- RELIANCE SMART ITEMS -----")
#         print("1. Rice  - ₹60/kg")
#         print("2. Sugar - ₹50/kg")
#         print("3. Oil   - ₹150/litre")
#
#     def shopping(self):
#         self.items()
#         self.total = 0
#
#         while True:
#             choice = input("\nEnter item (rice/sugar/oil): ").lower()
#             quantity = int(input("Enter quantity: "))
#
#             if choice == "rice":
#                 price = self.rice()
#             elif choice == "sugar":
#                 price = self.sugar()
#             elif choice == "oil":
#                 price = self.oil()
#             else:
#                 print("Item not available!")
#                 continue
#
#             amount = price * quantity
#             self.total += amount
#             print("Item added: ₹", amount)
#
#             more = input("Do you want to buy more? (yes/no): ").lower()
#
#             if more != "yes":
#                 break
#
#         self.billing()
#
#     def billing(self):
#         gst = self.total * 0.05
#         amount = self.total + gst
#
#         if amount > 2500:
#             discount = amount * 0.15
#         else:
#             discount = 0
#
#         final_amount = amount - discount
#
#         print("\n----- RELIANCE SMART BILL -----")
#         print("Shopping Amount : ₹", self.total)
#         print("GST (5%)        : ₹", gst)
#         print("Discount (15%)  : ₹", discount)
#         print("Final Bill      : ₹", final_amount)
#
#
# # Driver Code
#
# print("----- GROCERY SHOPPING -----")
# print("1. Dmart")
# print("2. Reliance Smart")
#
# choice = input("Choose supermarket: ")
#
# if choice == "1":
#     shop = Dmart()
#     shop.shopping()
#
# elif choice == "2":
#     shop = RelianceSmart()
#     shop.shopping()
#
# else:
#     print("Invalid choice!")
"""
 9. Bus Ticket Booking System Using Hierarchical Inheritance

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
#
# class Bus:
#     def sleeper(self):
#         return 800
#
#     def semi_sleeper(self):
#         return 600
#
#     def ac(self):
#         return 1000
#
#
# class RedBus(Bus):
#
#     def routes(self):
#         print("\n----- REDBUS ROUTES -----")
#         print("1. Hyderabad - Visakhapatnam")
#         print("2. Vijayawada - Hyderabad")
#         print("3. Visakhapatnam - Chennai")
#
#     def booking(self):
#         self.routes()
#
#         route = input("\nEnter route: ")
#
#         print("\nBus Types:")
#         print("1. Sleeper - ₹800")
#         print("2. Semi-Sleeper - ₹600")
#         print("3. AC - ₹1000")
#
#         choice = input("Choose bus type: ")
#         tickets = int(input("Enter number of tickets: "))
#
#         if choice == "1":
#             price = self.sleeper()
#         elif choice == "2":
#             price = self.semi_sleeper()
#         elif choice == "3":
#             price = self.ac()
#         else:
#             print("Invalid bus type!")
#             return
#
#         self.total = price * tickets
#
#         self.billing()
#
#     def billing(self):
#         gst = self.total * 0.10
#         reservation_charge = 30
#
#         final_amount = self.total + gst + reservation_charge
#
#         print("\n----- REDBUS BILL -----")
#         print("Ticket Amount      : ₹", self.total)
#         print("GST (10%)          : ₹", gst)
#         print("Reservation Charge : ₹", reservation_charge)
#         print("Total Amount       : ₹", final_amount)
#
#
# class AbhiBus(Bus):
#
#     def routes(self):
#         print("\n----- ABHIBUS ROUTES -----")
#         print("1. Hyderabad - Visakhapatnam")
#         print("2. Vijayawada - Hyderabad")
#         print("3. Visakhapatnam - Chennai")
#
#     def booking(self):
#         self.routes()
#
#         route = input("\nEnter route: ")
#
#         print("\nBus Types:")
#         print("1. Sleeper - ₹800")
#         print("2. Semi-Sleeper - ₹600")
#         print("3. AC - ₹1000")
#
#         choice = input("Choose bus type: ")
#         tickets = int(input("Enter number of tickets: "))
#
#         if choice == "1":
#             price = self.sleeper()
#         elif choice == "2":
#             price = self.semi_sleeper()
#         elif choice == "3":
#             price = self.ac()
#         else:
#             print("Invalid bus type!")
#             return
#
#         self.total = price * tickets
#
#         self.billing()
#
#     def billing(self):
#         gst = self.total * 0.10
#         reservation_charge = 20
#
#         final_amount = self.total + gst + reservation_charge
#
#         print("\n----- ABHIBUS BILL -----")
#         print("Ticket Amount      : ₹", self.total)
#         print("GST (10%)          : ₹", gst)
#         print("Reservation Charge : ₹", reservation_charge)
#         print("Total Amount       : ₹", final_amount)
#
#
# # Driver Code
#
# print("----- BUS TICKET BOOKING -----")
# print("1. RedBus")
# print("2. AbhiBus")
#
# choice = input("Choose platform: ")
#
# if choice == "1":
#     bus = RedBus()
#     bus.booking()
#
# elif choice == "2":
#     bus = AbhiBus()
#     bus.booking()
#
# else:
#     print("Invalid choice!")

""" 10. ATM System Using Multiple Inheritance

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
class SBI:
    def __init__(self):
        self.balance = 10000

    def deposit(self,amount):
        self.balance+=amount
        print("amount is deposited into your account")

    def check_balance(self):
        print("your balaance is: ",self.balance)

class UnionBank:
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
        else:
            print("insufficient balance")

    def mini_statement(self):
        print("Mini Statement")
        print("Current Balance: ₹", self.balance)

class ATM(SBI,UnionBank):
    def menu(self):
        print("\n----- ATM MENU -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Mini Statement")
        print("5. Exit")
    def transaction(self):
        while True:
            self.menu()
            choice=input("enter your option")
            if choice=="1":
                amount = float(input("Enter deposit amount: "))
                self.deposit(amount)
            elif choice=="2":
                amount = float(input("Enter withdraw amount: "))
                self.withdraw(amount)
            elif choice=="3":
                self.check_balance()
            elif choice=="4":
                self.mini_statement()
            else:
                print("Thank you for using ATM!")
                break
a1=ATM()
a1.transaction()
"""
 11. Paytm Application Using Multiple Inheritance

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
class MobileRecharge:

    def recharge_plans(self):
        print("\n----- RECHARGE PLANS -----")
        print("1. ₹199 - 1.5GB/day")
        print("2. ₹299 - 2GB/day")
        print("3. ₹399 - 2.5GB/day")

    def mobile_recharge(self):
        self.recharge_plans()

        choice = input("Choose recharge plan: ")

        if choice == "1":
            print("₹199 recharge successful!")

        elif choice == "2":
            print("₹299 recharge successful!")

        elif choice == "3":
            print("₹399 recharge successful!")

        else:
            print("Invalid plan!")


class BusTicketBooking:

    def display_buses(self):
        print("\n----- AVAILABLE BUSES -----")
        print("1. Hyderabad → Visakhapatnam")
        print("2. Vijayawada → Hyderabad")
        print("3. Visakhapatnam → Chennai")

    def book_ticket(self):
        self.display_buses()

        choice = input("Choose bus: ")
        tickets = int(input("Enter number of tickets: "))

        if choice == "1":
            price = 500
            route = "Hyderabad → Visakhapatnam"

        elif choice == "2":
            price = 400
            route = "Vijayawada → Hyderabad"

        elif choice == "3":
            price = 600
            route = "Visakhapatnam → Chennai"

        else:
            print("Invalid bus!")
            return

        total = price * tickets

        print("\n----- BUS BOOKING -----")
        print("Route:", route)
        print("Tickets:", tickets)
        print("Total Amount: ₹", total)
        print("Bus ticket booked successfully!")


class ElectricityBills:

    def bill_details(self):
        print("\n----- ELECTRICITY BILL -----")
        print("Electricity Provider: APSPDCL")

    def pay_bill(self):
        self.bill_details()

        amount = float(input("Enter bill amount: ₹"))

        print("Bill Amount: ₹", amount)
        print("Electricity bill paid successfully!")


class Paytm(MobileRecharge, BusTicketBooking, ElectricityBills):

    def menu(self):
        print("\n========== PAYTM ==========")
        print("1. Mobile Recharge")
        print("2. Bus Ticket Booking")
        print("3. Electricity Bill Payment")
        print("4. Exit")

    def services(self):

        while True:
            self.menu()

            choice = input("Choose a service: ")

            if choice == "1":
                self.mobile_recharge()

            elif choice == "2":
                self.book_ticket()

            elif choice == "3":
                self.pay_bill()

            elif choice == "4":
                print("Thank you for using Paytm!")
                break

            else:
                print("Invalid choice!")

paytm = Paytm()

paytm.services()


"""
______________composition______________
Composition → “has-a” relationship
One class contains/uses an object of another class.
Example: Car has an Engine
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
