# # class Vector:
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #
# #     def __add__(self, other):
# #         return Vector(self.x + other.x, self.y + other.y)
# #
# #     def __sub__(self, other):
# #         return (self.x - other.x, self.y - other.y)
# #
# #     def __mul__(self, other):
# #         return (self.x * other.x, self.y * other.y)
# #
# #     def __truediv__(self, other):
# #         return (self.x / other.x, self.y / other.y)
# #
# #     def __mod__(self, other):
# #         return (self.x % other.x, self.y % other.y)
# #     def __str__(self):
# #         return f'Vector({self.x},{self.y})'
# #
# #
# # V1 = Vector(10, 15)
# # V2 = Vector(9,3)
# # v3=Vector(3,5)
# #
# # print((V1 + V2)+v3)
# # print(V2 - V1)
# # print(V1 * V2)
# # print(V1 / V2)
# # print(V2 % V1)
# #
# #
# # class emp:
# #     def __init__(self,name,sal,dep):
# #         self.name=name
# #         self.sal=sal
# #         self.dep=dep
# #     def __gt__(self, other):
# #         return self.sal>other.sal
# #     def __ge__(self, other):
# #         return self.sal>=other.sal
# # e1=emp('ayaz',10000000,'SDE')
# # e2=emp('Chiru',1200000,'FD')
# # print(e1>e2)
# # print(e1<e2)
# #
# # print(e1>=e2)
# # print(e1<=e2)
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



