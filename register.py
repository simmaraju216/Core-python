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

# def apply(func, value):
#     return func(value)
#
#
# def double(x):
#     return x * 2
#
#
# def square(x):
#     return x * x
#
#
# a=apply(double, 5)
# print(a)# 10
# print(apply(square, 5))

def fun(x,y):
    z=[1,2,3]
    def fun2(a,b):
        print( a*y)
        print(b,z,sep='\n')
    return fun2
k=fun(20,40)
k(20,10)