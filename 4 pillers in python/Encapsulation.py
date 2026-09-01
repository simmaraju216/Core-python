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



class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
        self.setmarks(self.__marks)
    def setmarks(self,marks):
        if self.__marks>0 and self.__marks<=100:
            self.__marks=marks
        else:
            print("invalid marks")

    def getmarks(self):
        print(self.__marks)
s1=Student("raj",70)
s1.getmarks()
s1.setmarks(80)
s1.getmarks()