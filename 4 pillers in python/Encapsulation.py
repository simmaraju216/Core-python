"""
"""
"""
Encapsulation: Encapsulation means keeping data and the methods that operate on that data together inside a class,
 while controlling how that data can be accessed or modified. 
 
A. Data hiding
Preventing or discouraging outside code from directly accessing internal data.

B. Controlled access  
Providing methods or properties through which outside code can interact with that data.
"""
"""
| Syntax | Common terminology | Meaning                  |
| ------ | ------------------ | ------------------------ |
| x      | Public             | Can be accessed normally |
| _x     | Protected          | Internal-use convention  |
| __x    | Private            | Name mangling            |

"""
class A:
    def __init__(self):
        self._x=1000
    def m1(self):
        return self._x
    def setm1(self,new_val):
        self._x=new_val
a=A()
print(a.m1())
a.setm1(2000)
print(a.m1())
"""_____________________________________"""
"""
@property allows us to access a method like an attribute (variable), without using ().
@mathotname-means@property method.setter--->to change an attribute(variable) without using obj.method(val) insted obj.mathod=val
"""

class B:
    def __init__(self):
       self._x=200
    @property
    def y(self):
        return self._x
    @y.setter
    def z(self,nv):
        self._x=nv
b=B()
print(b.y)
b.z=300
print(b.z)

class Student:
    def __init__(self):
        self._marks = 0

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        self._marks = value
s = Student()

print(s.marks)   # GET → 0

s.marks = 90     # SET → calls the setter

print(s.marks)   # GET → 90
"""_____________________________________________"""
"""
Name mangling 
"""
class A:
    def __init__(self):
        self.__x = 100

a = A()

# print(a.__x)
""" it gives error because variable __x is private variabe so we an access "obj.currentclassname.variable" 
    print(a.__x)
          ^^^^^
AttributeError: 'A' object has no attribute '__x'
 """
print(a._A__x)


"""
1.  Create a BankAccount class that stores:
 • account number
 • balance (should not be directly modifiable) You must: 
    1. Make the balance attribute inaccessible from outside. 
    2. Provide functions to deposit/withdraw that validate the amount. 
    3. Prevent withdrawal if balance becomes negative.
    4. Show what happens if someone tries to modify balance directly and why encapsulation prevents it. 
"""

class BankAccount:
    def __init__(self,accountnumber,balance):
        self.accountnumber=accountnumber
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("you enter negative")
    def withdraw(self,wamount):
        if wamount<=0:
            print("withdraw amount is negative enter in positive")
        elif wamount>self.__balance:
            print("insufficient balance")
        else:
            self.__balance-=wamount
            print("withdraw successful")
    def checkbalance(self):
        print(self.__balance)
b1=BankAccount(12345,500)
b1.checkbalance()
b1.deposit(1000)
b1.checkbalance()
b1.withdraw(500)
b1.checkbalance()

"""
2. Design a Student class where marks: 
• should always be between 0 and 100 
• should never be set directly Enable updating marks only through a controlled method that performs range checks. 
Demonstrate: 
• trying to assign marks manually 
• why encapsulation protects invalid states 
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = None
        self.setmarks(marks)

    def setmarks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Marks must be between 0 and 100.")

    def getmarks(self):
        return self.__marks


# Create student
s1 = Student("Raj", 70)

print("Initial marks:", s1.getmarks())

# Update marks through controlled method
s1.setmarks(80)
print("Updated marks:", s1.getmarks())

# Try invalid marks
s1.setmarks(120)
print("Marks after invalid update:", s1.getmarks())

# Try direct assignment
s1.__marks = 150
print("Marks after direct assignment:", s1.getmarks())

"""
3. Create a SecureFile class that: 
• stores content privately 
• provides a method read(password) 
• refuses access if the password is incorrect 
• logs an "Unauthorized attempt" internally (cannot be accessed from outside) 
"""

class SecureFile:
    def __init__(self,content,password):
        self.__content=content
        self.__password=password
        self.__log=[]
    def read(self,password):
        if password==self.__password:
            return self.__content
        else:
            self.__log.append("Unauthorized attempt")
            return("Access denied")
f=SecureFile("raju",123)
print(f.read(123))
print(f.read(1234))

"""
4.Design an Employee class where: 
• salary is hidden 
• outsiders cannot read salary directly 
• use getter method that logs each access attempt 
• provide a method to update salary but only if the new salary is higher (prevent accidental downgrade) 
"""
class Employee:
    def __init__(self,salary):
        self.__salary=salary
        self.__log=[]
    def get_sal(self):
        self.__log.append("accessed")
        return self.__salary
    def set_sal(self,newsal):
        if newsal>self.__salary:
            self.__salary=newsal

e1=Employee(50000)
print(e1.get_sal())
e1.set_sal(60000)
print(e1.get_sal())
e1.set_sal(40000)
print(e1.get_sal())

"""
5. Create a Product class where: 
• price cannot be negative 
• discount cannot exceed 70% 
• internal final price calculation should not be directly exposed Provide only one public method get_final_price().
"""

class Product:
    def __init__(self, price, discount):
        if price < 0:
            print("Price cannot be negative")
            price = 0

        if discount > 70:
            print("Discount cannot exceed 70%")
            discount = 70

        self.__price = price
        self.__discount = discount

    def __calculate_final_price(self):
        return self.__price - (self.__price * self.__discount / 100)

    def get_final_price(self):
        return self.__calculate_final_price()

p1 = Product(1000, 20)

print(p1.get_final_price())

"""
6. Create a Character class with: 
• private _health 
• methods to damage(points) and heal(points) 
• health cannot drop below 0 or exceed max limit 
• expose only current health through a read-only getter 
"""
class Character:
    def __init__(self, health, max_health):
        self._health = health
        self.__max_health = max_health

    def damage(self, points):
        self._health -= points

        if self._health < 0:
            self._health = 0

    def heal(self, points):
        self._health += points

        if self._health > self.__max_health:
            self._health = self.__max_health

    def get_health(self):
        return self._health


# Create character
c1 = Character(100, 100)

print("Health:", c1.get_health())

c1.damage(30)
print("After damage:", c1.get_health())

c1.damage(100)
print("After heavy damage:", c1.get_health())

c1.heal(50)
print("After healing:", c1.get_health())

c1.heal(100)
print("After extra healing:", c1.get_health())

"""
*****  composition  *****
7. Create: 
• An Engine class with private state like temperature 
• A Car class that uses an Engine but should: 
 * Not allow users to manipulate engine temperature 
 * Only expose methods like start_car() or cool_engine() 
Demonstrate why giving direct engine access is dangerous. 
"""
class Engine:
    def __init__(self, temperature):
        self.__temperature = temperature

    def start(self):
        print("Engine started")

    def cool(self):
        self.__temperature -= 10

        if self.__temperature < 0:
            self.__temperature = 0

        print("Engine cooled")


class Car:
    def __init__(self):
        self.__engine = Engine(90)

    def start_car(self):
        self.__engine.start()

    def cool_engine(self):
        self.__engine.cool()

# Create car
c1 = Car()

c1.start_car()
c1.cool_engine()

"""
8. Create a ShoppingCart class where: 
• items are stored privately 
• users cannot directly modify item list 
• only add/remove methods are allowed 
• provide a method to get a safe copy of the cart items (not direct reference to internal list) 
"""

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def remove(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print("Item not found")

    def get_items(self):
        return self.__items.copy()
# Create cart
cart = ShoppingCart()

cart.add("Laptop")
cart.add("Mouse")
cart.add("Keyboard")

print("Cart:", cart.get_items())

cart.remove("Mouse")
print("After removing:", cart.get_items())

"""
Shallow Copy vs Deep Copy in Python

The main difference is what happens to nested objects.

1. Shallow Copy

A shallow copy creates a new outer object, but nested objects are still shared.
"""
import copy

original = [["Laptop", "Mouse"], ["Keyboard"]]

shallow = copy.copy(original)

shallow[0].append("Monitor")

print(original)
print(shallow)
"""
Output:

[['Laptop', 'Mouse', 'Monitor'], ['Keyboard']]
[['Laptop', 'Mouse', 'Monitor'], ['Keyboard']]

Why? The outer lists are different, but the inner list is the same object.

original ──→ [ ──→ ["Laptop", "Mouse"] ]
shallow  ──→ [ ──→ ["Laptop", "Mouse"] ]
                    ↑
                 shared
                 
"""
"""
2. Deep Copy

A deep copy creates a new outer object AND new nested objects.
"""

import copy

original = [["Laptop", "Mouse"], ["Keyboard"]]

deep = copy.deepcopy(original)

deep[0].append("Monitor")

print(original)
print(deep)
"""
Output:

[['Laptop', 'Mouse'], ['Keyboard']]
[['Laptop', 'Mouse', 'Monitor'], ['Keyboard']]

Now the nested lists are separate.

original ──→ [ ──→ ["Laptop", "Mouse"] ]

deep     ──→ [ ──→ ["Laptop", "Mouse", "Monitor"] ]
"""
"""
| Point                             | Shallow Copy                             | Deep Copy                              |
| --------------------------------- | ---------------------------------------- | -------------------------------------- |
| Outer object                      | Creates a new object                     | Creates a new object                   |
| Nested objects                    | **References are shared**                | **New copies are created**             |
| Memory                            | Uses less memory                         | Uses more memory                       |
| Speed                             | Generally faster                         | Generally slower                       |
| Changes to nested mutable objects | Can affect original                      | Do not affect original                 |
| Function                          | `copy.copy()`                            | `copy.deepcopy()`                      |
| Best use                          | When nested objects can safely be shared | When complete independence is required |
"""


"""
9. Implement a class incorrectly first: 
• Attendance stored in a list 
• Exposed directly so any outside code can modify it Then redesign properly: 
• Make attendance private 
• Provide controlled methods for marking attendance only Explain the difference. 
"""
"""
Incorrect implementation
"""
class Student:
    def __init__(self, name):
        self.name = name
        self.attendance = []

    def mark_attendance(self, date):
        self.attendance.append(date)


student = Student("Raju")

student.mark_attendance("2026-09-11")

print(student.attendance)

# Outside code can directly modify the list
student.attendance.append("Invalid Date")
student.attendance.clear()

print(student.attendance)

"""
Proper implementation
"""
class Student:
    def __init__(self, name):
        self.name = name
        self.__attendance = []

    def mark_attendance(self, date):
        if date not in self.__attendance:
            self.__attendance.append(date)
            print("Attendance marked")
        else:
            print("Attendance already marked")

    def get_attendance(self):
        return self.__attendance.copy()


student = Student("Raju")

student.mark_attendance("2026-09-11")
student.mark_attendance("2026-09-11")

print(student.get_attendance())