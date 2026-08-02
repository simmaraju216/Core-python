"""
A closure in Python is a function that remembers
 the variables from its outer (enclosing) function
 even after the outer function has finished executing.

Inner Function + Remembered Variables from Outer Function


Why do we need Closures?

Normally, when a function finishes executing, all its local variables are destroyed.

But sometimes we want an inner function to keep using those variables later.

"""
# def outer():
#
#     a = 10
#     b = 20
#     c=20
#     def inner():
#        print(a + b+c)
#
#     return inner
#
# f = outer()
# print(f)  #f is simply a variable that stores the function object returned by outer()
# # ,here f is the returned inner function object/address.
# """
# What is __closure__?
#
# It is a special attribute of a function.
# It stores all variables captured from the outer function.
# """
# print(f.__closure__)#Python stores it inside a cell object
# print(f.__closure__[0])# it means Give me the first cell object/address.
# print(f.__closure__[0].cell_contents)
# print(f.__closure__[1].cell_contents)
# """What is cell_contents?
# A cell object has a property called
# which returns whatever is inside the cell
# """
#
# """Decorators
# Decorators in Python are built using closures."""
# def decorato(func):
#     a = 10
#     b = 20
#     def wrapper():
#         print("Before")
#         print(a + b)
#         func()
#         print("After")
#
#     return wrapper
# @decorato
# def hello():
#     print("Hello")
# hello()


"""
Write a function electricity(rate_per_unit).

-   The outer function receives the cost per unit.
-   The inner function receives the number of units consumed.
-   Print the total electricity bill.
-   Return the inner function.
"""
def electricity(cost_per_unit):
    def innner(consumed_units):
        total_bill=cost_per_unit*consumed_units
        return total_bill
    return innner
e=electricity(20)
print(e(34))
print(e.__closure__[0].cell_contents)

"""
Write a function salary(bonus).

-   The outer function receives the bonus amount.
-   The inner function receives the employee’s basic salary.
-   Print the total salary after adding the bonus.
-   Return the inner function.

"""
def salary(bonus):
    def inner(emp_sal):
        return emp_sal+bonus
    return inner
x=salary(2000)
print(x(50000))

"""
Write a function discount(percent).
-   The outer function receives the discount percentage.
-   The inner function receives the product price.
-   Print the final price after applying the discount.
-   Return the inner function.

"""

def discount(percent):
    def inner(price):
        final_price=price-(percent/100)*price
        return final_price
    return inner
a=discount(10)
print(a(1000))


