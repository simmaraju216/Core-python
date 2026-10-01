""""""
"""
Exception handling ?

Exception handling in Python allows you to handle errors gracefully 
and take corrective actions without stopping the execution of the program
"""
"""
What Are Exceptions?
Exceptions are events that disrupt the normal flow of a program. 
They occur when an error is encountered during program execution. Common exceptions include:

- ZeroDivisionError: Dividing by zero.
- FileNotFoundError: File not found.
- ValueError: Invalid value.
- TypeError: Invalid type.


syntax:

try:
    # risky code
except:
    # handling code
"""
"""example """
try:
    a = 10
    b = 0
    print(a / b)
except:
    print("Something went wrong")

"""
Handling a Specific Exception:
"""
try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")


"""
Multiple except Blocks
"""
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Number cannot be zero")

"""
6. else Block
else executes only when there is no exception.

flow diagram 

try
 │
 ├── Error → except
 │
 └── No error → else
"""
try:
    num = int(input("Enter number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

"""
finally Block

finally executes whether an exception occurs or not.

Why use finally?

Usually for cleanup operations:

Closing files
Closing database connections
Releasing resources
"""
try:
    num = 10 / 2
    print(num)

except ZeroDivisionError:
    print("Error")

finally:
    print("Program completed")



"""
raise Keyword

raise is used when you want to manually generate an exception
"""
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount

print(withdraw(5000, 6000))

"""
Custom Exception
"""
"""
We can create our own exception class.
"""

class InsufficientBalanceError(Exception):
    pass

balance = 5000
withdraw = 6000

try:
    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient balance")

except InsufficientBalanceError as e:
    print(e)


"""
Error vs Exception

Error
An error is a problem that prevents the program from working correctly.

ex: 
SyntaxError
IndentationError

Exception
An exception occurs during program execution and can often be handled using try-except.

ex:
ValueError
TypeError
ZeroDivisionError
IndexError
KeyError



Error
  ↓
Problem in program

Exception
  ↓
Runtime problem
  ↓
Can often be handled
"""

try:
    username = input("Username: ")
    password = input("Password: ")

    if username == "":
        raise ValueError("Username cannot be empty")

    if password == "":
        raise ValueError("Password cannot be empty")

    print("Login successful")

except ValueError as e:
    print("Login failed:", e)

finally:
    print("Login process completed")



# 1
# from koji_cli.lib import print_task
# from oci.exceptions import ServiceError


# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter another number: "))
#     c=a/x
# except ValueError as ve:
#     print(ve)AX
# except ZeroDivisionError as zd:
#     print("b cannot be zero")
# except Exception as ex:
#     print(ex)
# else:
#     print(c)
# finally:
#     print("reached end of code")

# def fun(x,y):
#     try:
#         return int(x)/int(y)
#     except ValueError as ve:
#         raise TypeError("test chesthunna")
#     except ZeroDivisionError as zd:
#         print("b cannot be zero")
#
# print(fun(input(),input()))
# print(fun(input(),input()))
# print(fun(input(),input()))

# custom exception/error

# a=int(input())
# if a<0:
#     a=ValueError("a cannot be negative")
#     raise a

# custom exception class
# class AgeError(ValueError):
#     pass
#
# age=int(input())
# if age<18:
#     raise AgeError("age cannot be less than 18")


#
# • Create a class Person whose constructor takes age as an argument. Raise a
# ValueError if the age is less than 0.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         if age<0:
#             raise ValueError("age must be positive")
#         self.age = age
# p1=Person("John", 18)
# p2=Person("John", -18)


# • Write a function named find_length(obj) that uses a loop to calculate the
# length of the given object without using the built-in len() function. The
# function should return the calculated length if the object is iterable. If a
# non-iterable object such as an integer is passed, the function should raise and
# handle a TypeError, and print an appropriate error message explaining what
# happens when an integer is sent as input.

def find_length(obj):
    c=0
    if isinstance(obj, (str,list,tuple,set)):
        for i in obj:
            c+=1
    elif isinstance(obj,dict):
        for i,j in obj.items():
            c+=1
    else:
        raise TypeError("obj must be a string,list,tuple,set")
    return c
# print(find_length(1))
print(find_length([1,2,3,4,5,5,8]))
print(find_length({1,2,3,4,5,5,8}))
print(find_length((1,2,3,4,5,5,8)))


# • Create a class Student with an attribute marks. Implement a method
# set_marks(marks) that raises a ValueError if marks are not in the range 0 to
# 100.

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def setmarks(self,marks):
        if marks>100 or marks<0:
            raise ValueError("marks must be between 0 and 100")
        self.marks=marks
s1=Student("John",25)
# s1.setmarks(-25)

# • Create a custom exception named InvalidAgeError. Create a class Voter with a
# method check_eligibility(age) that raises this exception if age is less than 18.
# --done

# • Create a class BankAccount with an attribute balance. Implement a method
# withdraw(amount) that raises an exception if the withdrawal amount is greater
# than the available balance.

class InsufficientBalance(Exception):
    pass

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def withdraw(self,amount):
        if amount>self.balance:
            raise InsufficientBalance("paisal levvu")
        self.balance-=amount
b1=BankAccount("John",25000000)
# b1.withdraw(100000000000)



# • Create a class PasswordValidator with a method validate(password). Raise an
# exception if the password length is less than 8 characters.

class Passwordvalidator:
    def validate(self,password):
        if len(password) < 8:
            raise ValueError("password must be at least 8 characters long")
        print("validation successful")
p1=Passwordvalidator()
# p1.validate("")

# • Create a class UserInput with a method get_integer(value). Handle ValueError
# and TypeError using separate except blocks.

class UserInput:
    def get_integer(self,value):
        return int(value)

try:
    a=input("enter value: ")
    l=[1,2,23,4]
    UserInput().get_integer(l)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
# • Create a base class Shape with a method area() that raises
# NotImplementedError. Create a child class Rectangle that overrides and
# implements the area method.
# --done

# • Create a class Service with a method that calls another method which raises an
# exception. Catch and handle the exception in the Service class.
class ServiceError(Exception):
    pass
class Service:
    def m1(self):
        raise ServiceError("Service m1")
    def m2(self):
        self.m1()
try:
    service=Service()
    service.m1()
except ServiceError as e:
    print(e)

# • Create a class Transaction with a method process() that uses try, except, and
# finally blocks to ensure a cleanup message is always printed.

class Transaction:
    def process(self):
        try:
            print("transaction started")
            raise ServiceError("Service error in process method")
        except ServiceError as e:
            print(e)
t1=Transaction()
t1.process()

# • Create a class LoginSystem with a method login(password) that raises an
# exception for an incorrect password and handles the exception outside the class
# done