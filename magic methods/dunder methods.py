class student:
    def __init__(self,name,age,clg):
        self.name=name
        self.age=age
        self.clg=clg
    def __str__(self):      # for direct representation of object
        return f"My name is {self.name},age is {self.age},my clg name is {self.clg}." # to print description about object
    def __repr__(self):     # for direct and indirect representation of object
        return f'{self.name}'
s1=student('ayaz',21,'SR')
s2=student('priya',20,'MRU')
print(s1)
print(s2)
l=[s1,s2]
print(l)
print(*l)


"""# Singleton class -> Even if we create multiple objects,
# it returns the same object (same memory address).

Singleton Class: A class that allows only one object to be created. Whenever multiple objects are created,
the same object instance is returned. This is commonly implemented by overriding the __new__() method.
"""
class A:
    x = None

    def __new__(cls):
        if cls.x is None:
            cls.x = super().__new__(cls)
        return cls.x

obj1 = A()
print(obj1)

obj2 = A()
print(obj2)

print(obj1 is obj2)   # True
print(id(obj1))
print(id(obj2))



"""
1. Create a class called Product with attributes name and price. 
Change the + operator so that adding two Product objects returns the sum of their prices.

p1 = Product("Keyboard", 1500)
p2 = Product("Mouse", 700)
print(p1 + p2)

Expected Output:
2200

"""

class Product:
    def __init__(self,pname,price):
        self.pname=pname
        self.price=price
    def __add__(self, other):
        return self.price+other.price
p1 = Product("Keyboard", 1500)
p2 = Product("Mouse", 700)

print(p1 + p2)



"""
2. Create a class called BankAccount with an attribute balance. 
Change the - operator so that subtracting one account from another returns the difference between their balances.

account1 = BankAccount(10000)
account2 = BankAccount(3500)
print(account1 - account2)

Expected Output:
6500

Operator to change: -
Magic Method: _sub_()
"""

class BankAccount:
    def __init__(self,amount):
        self.amount=amount

    def __sub__(self, other):
        return self.amount-other.amount

account1 = BankAccount(10000)
account2 = BankAccount(3500)
print(account1 - account2)

"""
3. Create a class called ShoppingCart with an attribute total. 
Change the * operator so that multiplying a cart by an integer returns the total cost for that many identical carts.

cart = ShoppingCart(2500)
print(cart * 3)

Expected Output:
7500

Operator to change: *
Magic Method: _mul_()
"""

class ShoppingCart:
    def __init__(self,price):
        self.price=price
    def __mul__(self, other):
        return self.price*other
cart = ShoppingCart(2500)
print(cart*3)

"""
4. Create a class called Bill with an attribute amount. 
Change the / operator so that dividing a Bill object by a number returns the amount each person must pay.

bill = Bill(1200)
print(bill / 4)

Expected Output:
300.0

Operator to change: /
Magic Method: _truediv_()
"""

class Bill:
    def __init__(self,amount):
        self.amount=amount

    def __truediv__(self, other):
        return self.amount/other

bill = Bill(1200)
print(bill / 4)

"""
5. Create a class called Student with attributes name and marks. 
Change the > operator so that one student is considered greater than another when their marks are higher.

student1 = Student("Anil", 85)
student2 = Student("Ravi", 72)
print(student1 > student2)

Expected Output:
True

Operator to change: >
Magic Method: _gt_()

"""

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self, other):
        return self.marks>other.marks

student1 = Student("Anil", 85)
student2 = Student("Ravi", 72)
print(student1 > student2)