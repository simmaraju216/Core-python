s='hello'
k=iter(s)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
"""______________"""
e=iter(s)
print(next(e))
print(next(e))
print(next(e))
print(next(e))
#
"""_______________________________"""
class B:
    def __init__(self,s,e):
        self.start=s
        self.end=e
    def __iter__(self):
        return self
    def __next__(self):
        if self .start>self.end:
            raise StopIteration
        v=self.start
        self.start+=1
        return v

b1=B(10,20)
k=iter(b1)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
# __________or ______________
for i in b1:
    print(i)

#Write a custom iterator that prints numbers from 1 to N.

class A:
    def __init__(self,n):
        self.n=n
        self.st=1
    def __iter__(self):
        return  self
    def __next__(self):
        if self.st>self.n:
            raise StopIteration
        x=self.st
        self.st+=1
        return x
k=int(input())
a1=A(k)
for i in a1:
    print(i)
"""------------------------------------------"""
class C:
    def __init__(self,l):
        self.l=l
        self.pos=0
    def __iter__(self):
        return self
    def __next__(self):
        while (self.pos<len(self.l)):
            x=self.l[self.pos]
            self.pos += 1
            if x%2==0:
                return x
        raise StopIteration
k=[1,3,20,4,5,60,78,45,33,29,75,88]
c1=C(k)
for i in c1:
    print(i)


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
#
class EvenNumbers:
    def __init__(self,start, count):
        self.start=start
        self.count=count
    def __iter__(self):
        return self
    def __next__(self):
        while( self.start<self.count):
            v=self.start
            self.start+=1
            if v%2==0:
                return v
        raise StopIteration
even=EvenNumbers(1,20)
# k=iter(even)
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
for i in even:
    print(i)
"""----------------------------------"""
class Countdown:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n<=0:
            raise StopIteration
        v=self.n
        self.n-=1
        return v
c=Countdown(10)
k=iter(c)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
try:
    while True:
        print(next(k))
except StopIteration:
    print("Done")

for i in c:
    print(i)
"""________________________________________________"""

"""Write a custom iterator class EvenNumbers(start, count) 
that yields count even numbers starting from start.
 Implement __iter__ and __next__ correctly. 
 Demonstrate with a for loop and with manual next() calls.
"""
class EvenNumbers:
    def __init__(self, start, count):
        self.start = start
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        while self.count > 0:
            if self.start % 2 == 0:
                v = self.start
                self.start += 1
                self.count -= 1
                return v
            self.start += 1
        raise StopIteration


a = EvenNumbers(1, 20)

for i in a:
    print(i)

"""Write a function simulate_for_loop(iterable) that replicates
 what Python's for loop does internally — using iter() and next() and catching StopIteration. 
Test it on a list, a string, and your custom EvenNumbers iterator from Q1
"""

class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            v = self.start
            self.start += 1
            if v % 2 == 0:
                return v
        raise StopIteration


def simulate_for_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            item = next(iterator)
            print(item)
        except StopIteration:
            break
# print("list:")
simulate_for_loop([1,2,3,4,5,6,7])
# print("/nstring")
simulate_for_loop("python")
# k=[11,22,33,44,55]
# print("list:")
simulate_for_loop(EvenNumbers(1,20))
# print(k)


