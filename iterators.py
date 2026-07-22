# s='hello'
# k=iter(s)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
#
# e=iter(s)
# print(next(e))
# print(next(e))
# print(next(e))
#
#
# class B:
#     def __init__(self,s,e):
#         self.start=s
#         self.end=e
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self .start<=self.end:
#             self.start+=1
#             return self.start
#     # raise stopiteration
# b1=B(10,20)
# k=iter(b1)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))



#Write a custom iterator that prints numbers from 1 to N.

# class A:
#     def __init__(self,n):
#         self.n=n
#         self.st=1
#     def __iter__(self):
#         return  self
#     def __next__(self):
#         if self.st>self.n:
#             raise StopIteration
#         x=self.st
#         self.st+=1
#         return x
# k=int(input())
# a1=A(k)
# for i in a1:
#     print(i)

# class C:
#     def __init__(self,l):
#         self.l=l
#         self.pos=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while (self.pos<len(self.l)):
#             x=self.l[self.pos]
#             self.pos += 1
#             if x%2==0:
#                 return x
#         raise StopIteration
# k=[1,3,20,4,5,60,78,45,33,29,75,88]
# c1=C(k)
# for i in c1:
#     print(i)


#
# class D:
#     def __init__(self,s):
#         self.s=s
#         self.pos=len(s)-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.pos<0:
#             raise StopIteration
#         x=self.s[self.pos]
#         self.pos-=1
#         return x
# k='Raju'
# d1=D(k)
# for i in d1:
#     print(i)


#
# class E:
#     def __init__(self,s):
#         self.s=s
#         self.pos=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.pos>=len(self.s):
#             raise StopIteration
#         x=self.s[self.pos]
#         self.pos += 1
#         return x
# k='Raju'
# e1=E(k)
# for i in e1:
#     print(i)
# #_____________or________________
# class E:
#     def __init__(self, s):
#         self.s = s
#         self.pos = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.pos < len(self.s):
#             if self.pos % 2 == 0:
#                 x = self.s[self.pos]
#                 self.pos += 1
#                 return x
#             self.pos += 1
#         raise StopIteration
#
# k = "Raju"
# e1 = E(k)
#
# for i in e1:
#     print(i)