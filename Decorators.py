# def fun(x):
#     def inner():
#         print('hello')
#     return inner
# @fun
# def fun3():
#     print('hii')
# fun3()
# import functools


# def dec(func):
#     print('fun called')
#     def inner():
#         print('starting fun')
#         print(f'func:{func.__name__}')
#         func()
#         print('ending fun')
#     return inner
# @dec
# def greet():
#     print('hello')
# greet()
# print(f'greet:{greet.__name__}')
#


# def login(func):
#     us={'teju':'123','ram':'234','jam':'789'}
#     def inner():
#         user=input('enter user')
#         password=input('enter password')
#         if user in us.keys():
#             if password==us[user]:
#                 print('login success')
#                 func()
#             else:
#                 print('wrong password')
#         else:
#             print('no user')
#     inner()
# @login
# def file():
#     print('secure file')

# def Dec(func):
#     print("Function Called")
#     def Inner():
#         print("Starting Function")
#         print(f"Func : {func.__name__}")
#         func()
#         print("Ending Function")
#     return Inner
#
# @Dec
# def greet():
#     print("hello Bro")
#
# # greet()
# # print(f"greet : {greet.__name__}")
#
# def login(func):
#     us = {"teju":"teju123","peddi":"Cherry","chiru":"Raju"}
#     def Inner():
#         user = input("Enter your username: ")
#         password = input("Enter your password: ")
#         if user in us.keys():
#             if password == us[user]:
#                 print("Login Successful")
#                 func()
#             else:
#                 print("Wrong Password")
#         else:
#             print("User not found")
#     return Inner
#
# @login
# def file():
#     print("Secured File")
#
# # file()
#
# def valid(func):
#     def inner(name,place,age,gender,mail,phno):
#         if isinstance(age,int) and '@gmail.com' in mail and 14 <= len(phno) >= 10 and gender in ("Male", "Female", "other"):
#             func(name,place,age,gender,mail,phno)
#         else:
#             print("Registration Unsuccessful")
#     return inner
#
# @valid
# def Register(name,place,age,gender,mail,phno):
#     print("Register Successful")
#
# Register("Pavan","markapur",20,'Male','pavan@gmail.com','+91-9014432634')
#__________annotations________________
# def fun(a:str,b:str)->str:
#     """this is doc string"""
#     return a+b
# print(fun.__annotations__)
# print(fun.__doc__)
# print(print.__doc__)
"""________________________________________"""
import functools
# def valid(func):
#     @functools.wraps(func)
#     def inner(a,b):
#         if not isinstance(a,str):
#             a=str(a)
#         if not isinstance(b,str):
#             b=str(b)
#         return func(a,b)
#     return inner
# @valid
# def fun(a:str,b:str)->str:
#     """this is doc string"""
#     return a+b
# print(fun("12","23"))
# print(fun.__name__)
# print(fun.__annotations__)
# print(fun.__doc__)
# """_______________________________________________"""
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Function is being called")
#         return func(*args, **kwargs)
#     return wrapper
#
# @my_decorator
# def add(a, b):
#     return a + b
#
# print(add(3, 5))
# """______________________________________________"""
# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat(3)
# def greet():
#     print("Hello")
#
# greet()
# """___________________________________________________"""
# import functools
#
#
# def prefix_log(prefix, separator=' | '):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             print(f'{prefix}{separator}{result}')
#             return result
#
#         return wrapper
#
#     return decorator
# @prefix_log('INFO')
# def get_status():
#     return 'Server is running'
#
# @prefix_log('ERROR', separator=' --> ')
# def get_error():
#     return '404 Not Found'
#
# get_status()
# get_error()

"""_________________________________________________"""
def logger(func):
    def wrapper():
        print("Logger: Before function")
        func()
        print("Logger: After function")
    return wrapper

def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(1,n+1):
                print(f"Repeat {i}")
                func()
        return wrapper
    return decorator
@repeat(3)
@logger
def greet():
    print("Hello")
greet()
"""_______________________________________"""
# def count_calls(n):
#     def dec(func):
#
# @count_calls(3)
# def great():
#
