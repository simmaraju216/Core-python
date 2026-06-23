#_____________practice section1____________
def say_hello(): #1
    return 'Welcome to Python!'
print(say_hello())

# 2
def add(a,b):
    return(a+b)
print(add(10,26))

# 4
def area_of_rectangle(l,b):
    return l*b
print(area_of_rectangle(6,4))

#________________practice section2____________
#Paraamaters__________________________
#1
def multiply(a,b,c):
    return a*b*c
a=int(input())
b=int(input())
c=int(input())
print(multiply(a,b,c))

#2
def describe_pet(animal,name):
    print(f'my {animal} is named {name}')
animal=input()
name=input()
describe_pet(animal, name)

#3
def fun(a,b,c,d):
    print(a,b,c,d)
fun(10,20)   #TypeError: fun() missing 2 required positional arguments: 'c' and 'd'

#4
def power(base,exponent):
    return base**exponent
print(power(2,3))

#5
def full_name(first,middle,last):
    return(first+" "+middle+" "+last)
first=input()
middle=input()
last=input()
print(full_name(first,middle,last))

#________________practice section3____________
#________Positional Arguments_____________
#1
def intro(name,city,hobby):
    return(f'i am {name} i am from {city} my hobby is {hobby}')
print(intro('Raju','Srikakulam','playing cricket'))
print(intro('Chiru','Vizianagaram','playing chess'))

#2
def substract(a,b):
    return a-b
print(substract(10,3))
print(substract(3,10))

#________________practice section4____________
def send_email(to,subjet,body):
    print(to)
    print(subjet)
    print(body)
send_email(to='Chiru',body='''Udemy is a US-based education technology company.''' ,subjet= 'Good Morning')
