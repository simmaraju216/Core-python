""" """
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         return (self.x - other.x, self.y - other.y)
#
#     def __mul__(self, other):
#         return (self.x * other.x, self.y * other.y)
#
#     def __truediv__(self, other):
#         return (self.x / other.x, self.y / other.y)
#
#     def __mod__(self, other):
#         return (self.x % other.x, self.y % other.y)
#     def __str__(self):
#         return f'Vector({self.x},{self.y})'
#
#
# V1 = Vector(10, 15)
# V2 = Vector(9,3)
# v3=Vector(3,5)
#
# print((V1 + V2)+v3)
# print(V2 - V1)
# print(V1 * V2)
# print(V1 / V2)
# print(V2 % V1)
#
#
# class emp:
#     def __init__(self,name,sal,dep):
#         self.name=name
#         self.sal=sal
#         self.dep=dep
#     def __gt__(self, other):
#         return self.sal>other.sal
#     def __ge__(self, other):
#         return self.sal>=other.sal
# e1=emp('ayaz',10000000,'SDE')
# e2=emp('Chiru',1200000,'FD')
# print(e1>e2)
# print(e1<e2)
#
# print(e1>=e2)
# print(e1<=e2)
#
# class inventory:
#     total_items=0
#     def __init__(self):
#         self.li=[]
#     def __add__(self, other):
#         if isinstance(other,str):
#             self.li.append(other)
#             inventory.total_items+=1
#             return(self)
#     def __len__(self):
#         return len(self.li)
#     def __contains__(self, item):
#         return item in self.li
# i1=inventory()
# i2=inventory()
# print(i1+"marker"+'pencil'+'pen')
# print(len(i1))
# print('marker'in i1)

"""
____________extre magic methods___________
"""
class Student:
    def _init_(self, name, age):
        self.name = name
        self.age = age
        self.data={}
    def _eq_(self, other):
        return self.name == other.name
    def _hash_(self):
        return hash(self.name)
    def _getitem_(self, item):
        return self.data[item]
    def _setitem_(self, key, value):
        self.data[key] = value

    def _getattribute_(self, item):
        print(f"getting attribute {item}")
        return super()._getattribute_(item)
    def _getattr_(self, item):
        print(f"getting attribute using attr {item}")
        return "testing with something"

s1=Student('John', 25)
s2=Student('John', 28)
print(s1.x)




# s1['name']="XYZ"
# print(s1['name'])
# del s1.age
# print(s1.age)
# del s1['name']
# print(s1.name)

# s1['name']="John"
# print(s1["name"])

#
# print(s1==s2)
# #
# print(hash(s1))
# print(hash(s2))





l=[]

class Product:
    def _init_(self, name, price):
        self.name = name
        self.price = price

    def _contains_(self, item):
        return self in item


obj=Product("test1",200)
obj1=Product("test2",200)
l.append(obj)
print(obj1 in l)
l.append(obj1)
print(obj1 in l)


