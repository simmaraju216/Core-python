# #_____________practice section1____________
# def say_hello(): #1
#     return 'Welcome to Python!'
# print(say_hello())
#
# # 2
# def add(a,b):
#     return(a+b)
# print(add(10,26))
#
# # 4
# def area_of_rectangle(l,b):
#     return l*b
# print(area_of_rectangle(6,4))
#
# #________________practice section2____________
# #Paraamaters__________________________
# #1
# def multiply(a,b,c):
#     return a*b*c
# a=int(input())
# b=int(input())
# c=int(input())
# print(multiply(a,b,c))
#
# #2
# def describe_pet(animal,name):
#     print(f'my {animal} is named {name}')
# animal=input()
# name=input()
# describe_pet(animal, name)
#
# #3
# def fun(a,b,c,d):
#     print(a,b,c,d)
# fun(10,20)   #TypeError: fun() missing 2 required positional arguments: 'c' and 'd'
#
# #4
# def power(base,exponent):
#     return base**exponent
# print(power(2,3))
#
# #5
# def full_name(first,middle,last):
#     return(first+" "+middle+" "+last)
# first=input()
# middle=input()
# last=input()
# print(full_name(first,middle,last))
#
# #________________practice section3____________
# #________Positional Arguments_____________
# #1
# def intro(name,city,hobby):
#     return(f'i am {name} i am from {city} my hobby is {hobby}')
# print(intro('Raju','Srikakulam','playing cricket'))
# print(intro('Chiru','Vizianagaram','playing chess'))
#
# #2
# def substract(a,b):
#     return a-b
# print(substract(10,3))
# print(substract(3,10))
#
# #________________practice section4____________
# def send_email(to,subjet,body):
#     print(to)
#     print(subjet)
#     print(body)
# send_email(to='Chiru',body='''Udemy is a US-based education technology company.''' ,subjet= 'Good Morning')


#________________practice section 6____________
# ===========================
# Q1. multiply_all(*args)
# ===========================
#
# def multiply_all(*args):
#     product = 1
#     for num in args:
#         product *= num
#     return product
#
# print("Q1 Output:")
# print("Product =", multiply_all(2, 3, 4))
# print()
#
#
# # ===========================
# # Q2. display_tags(**kwargs)
# # ===========================
#
# def display_tags(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
#
# print("Q2 Output:")
# display_tags(name="Raju", age=20, course="Python")
# print()
#
#
# # ===========================
# # Q3. describe_person(name, *hobbies)
# # ===========================
#
# def describe_person(name, *hobbies):
#     print("Name :", name)
#     print("Hobbies :", hobbies)
#
# print("Q3 Output:")
# describe_person("Raju", "Cricket", "Cooking", "Reading")
# print()
#
#
# # ===========================
# # Q4. *args Type
# # ===========================
#
# def f(*args):
#     print(type(args))
#
# print("Q4 Output:")
# f(1, 2, 3)
#
# print("\nExplanation:")
# print("*args collects all positional arguments into a tuple.")
# print()
#
#
# # ===========================
# # Q5. create_html_tag(tag, **attributes)
# # ===========================
#
# def create_html_tag(tag, **attributes):
#     html = f"<{tag}"
#
#     for key, value in attributes.items():
#         html += f" {key}='{value}'"
#
#     html += ">"
#     print(html)
#
# print("Q5 Output:")
# create_html_tag(
#     "a",
#     href="https://python.org",
#     target="_blank"
# )
# print()
#
#
# # ===========================
# # Q6. mixed(a, b, *args, **kwargs)
# # ===========================
#
# def mixed(a, b, *args, **kwargs):
#     print("a =", a)
#     print("b =", b)
#     print("*args =", args)
#     print("**kwargs =", kwargs)
#
# print("Q6 Output:")
# mixed(
#     10,
#     20,
#     30,
#     40,
#     50,
#     name="Raju",
#     age=20,
#     city="Srikakulam"
# )

# section 6__________________
# ==========================================
# Q1. Assign len to a variable called count.
# ==========================================

count = len

numbers = [10, 20, 30, 40, 50]

print("Q1 Output:")
print("Length of list =", count(numbers))
print()


# ==========================================
# Q2. run_twice(func, value)
# ==========================================

def run_twice(func, value):
    return func(func(value))

def square(x):
    return x * x

print("Q2 Output:")
print(run_twice(square, 2))     # square(square(2))
print()


# ==========================================
# Q3. Store upper, lower, title in dictionary
# ==========================================

operations = {
    "upper": str.upper,
    "lower": str.lower,
    "title": str.title
}

choice = input("Enter (upper/lower/title): ")
text = input("Enter a string: ")

print("Q3 Output:")
if choice in operations:
    print(operations[choice](text))
else:
    print("Invalid Choice")
print()


# ==========================================
# Q4. Function returning another function
# ==========================================

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

triple = make_multiplier(3)

print("Q4 Output:")
print(triple(5))
print()


# ==========================================
# Q5. Store same function under multiple names
# ==========================================

def greet(name):
    return "Hello " + name

functions = {
    "hello": greet,
    "welcome": greet,
    "hi": greet
}

print("Q5 Output:")
print(functions["hello"]("Raju"))
print(functions["welcome"]("Raju"))
print(functions["hi"]("Raju"))

print("\nExplanation:")
print("The same function object can be stored under multiple keys.")
print("All keys refer to the same function and produce the same output.")