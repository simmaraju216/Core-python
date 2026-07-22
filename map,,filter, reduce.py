# def add(a,b):
#     return a+b    #Normal function
# x=10
# y=20
# print(add(x,y))
# """_______________________________________"""
# l=lambda x,y:x+y  #lambda function
# print(l(x,y))
# """_________________Higher order functions_________________________"""
# f=[1,2,3,4,5,6,7,8,9]
# """map()
# syntax: map(functional reference,iterable value/object)"""
# k=list(map(lambda x:x+5,f))
# print(k)
# """filter()
# syntax: filter(functional reference,iterable value/object)"""
# m=list(filter(lambda x:x%2==0,k))
# print(m)
# """reduce()
# syntax: reduce(functional reference,iterable value/object,initial val(optional)"""
# from functools import reduce
# x=reduce(lambda a,b:a+b,m)
# print(x)
# """sorted()
# syntax: sorted(iterable value/object,key=functional reference))"""
# s=sorted(m,key=lambda x:x,reverse=True)
# print(s)
# a=[1,2,3,4]
# b=[10,20,30,40]
# m=list(map(lambda x,y:x+y,a,b))
# print(*m)
#
# nums = [12, 15, 7, 18, 20, 21, 25]
# n=list(filter(lambda x:(x%3==0)!=(x%5==0) ,nums))
# print(n)
#
# from functools import reduce
# l=[1, 2, 3, 4]
# s=0
# k=reduce(lambda x,y:x+y,l,10)
# print(k)
# #
# nums = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda x: x.append(10),nums))
# print("Result:", result)
# print("Nums:", nums)
# #
# d = {"apple": 100, "banana": 40, "cherry": 150}
# k = dict(filter(lambda x: x[1] > 50, d.items()))
# print(k)
#
# d = {"apple": 100, "banana": 40, "cherry": 150}
# k = list(filter(lambda x: d[x] > 50, d))
# print(k)
#
#
# from functools import reduce
# p=['P', 'y', 't', 'h', 'o', 'n']
# o=reduce(lambda x,y:x+y,p)
# print(o)
#
#
# x=list(map(lambda x:id(x),[10, 350, 10, 350, 20]))
# print(x)
#
# l=['Hello','Hii','Who','are','you?']  #in"AEIOUaeiou"
# m=list(map(lambda x:list(filter(lambda ch:ch not in "AEIOUaeiou",x)),l))
# print(m)
# l1=[]
# for i in m:
#     k=list(map(ord,i))
#     l1.append(sum(k))
# print(l1)
# print(sum(l1))
# """_______________or_________________"""
# # for i in l:
# #     m=list(map(lambda x:x if x not in "AEIOUaeiou"else '',i))
# #     print(m)
#
#
#
# # ==========================================
# # Section 8: Lambda Functions
# # ==========================================
#
# # ==========================================
# # Q1. Lambda function to return cube
# # ==========================================
#
# cube = lambda x: x ** 3
#
# print("Q1 Output:")
# print(cube(3))
# print()
#
#
# # ==========================================
# # Q2. Lambda to return larger number
# # ==========================================
#
# largest = lambda x, y: x if x > y else y
#
# print("Q2 Output:")
# print(largest(15, 20))
# print()
#
#
# # ==========================================
# # Q3. Convert regular function into lambda
# # ==========================================
#
# # Regular Function
# # def even(n):
# #     return n % 2 == 0
#
# even = lambda n: n % 2 == 0
#
# print("Q3 Output:")
# print(even(8))
# print(even(7))
# print()
#
#
# # ==========================================
# # Q4. Sort list of tuples by second element
# # ==========================================
#
# fruits = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]
#
# fruits.sort(key=lambda x: x[1])
#
# print("Q4 Output:")
# print(fruits)
# print()
#
#
# # ==========================================
# # Q5. Lambda calling another function
# # ==========================================
#
# def square(x):
#     return x * x
#
# result = lambda n: square(n) + 10
#
# print("Q5 Output:")
# print(result(5))
# print()
#
#
# # ==========================================
# # Q6. Limitations of Lambda
# # ==========================================
#
# print("Q6 Output:")
# print("1. Lambda can contain only one expression.")
# print("2. Lambda cannot contain multiple statements like loops or if-else blocks.")
# print("3. Lambda cannot use statements such as return, break, continue, or pass.")
#
#
#
# # ==========================================
# # Section 9: map(), filter(), reduce()
# # ==========================================
#
# from functools import reduce
#
# # ==========================================
# # Q1. Convert Celsius to Fahrenheit using map()
# # Formula: F = (C × 9/5) + 32
# # ==========================================
#
# celsius = [0, 20, 30, 40]
#
# fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
#
# print("Q1 Output:")
# print(fahrenheit)
# print()
#
#
# # ==========================================
# # Q2. Extract words starting with a capital letter
# # ==========================================
#
# words = ["Apple", "banana", "Cat", "dog", "Elephant", "fish"]
#
# capital_words = list(filter(lambda word: word[0].isupper(), words))
#
# print("Q2 Output:")
# print(capital_words)
# print()
#
#
# # ==========================================
# # Q3. Product of all numbers using reduce()
# # ==========================================
#
# numbers = [1, 2, 3, 4, 5]
#
# product = reduce(lambda x, y: x * y, numbers)
#
# print("Q3 Output:")
# print(product)
# print()
#
#
# # ==========================================
# # Q4. Sort tuples by age (descending)
# # ==========================================
#
# people = [
#     ("Raju", 20),
#     ("Anil", 25),
#     ("Sita", 18),
#     ("Kiran", 22)
# ]
#
# sorted_people = sorted(people, key=lambda x: x[1], reverse=True)
#
# print("Q4 Output:")
# print(sorted_people)
# print()
#
#
# # ==========================================
# # Q5. Filter even numbers, then square them
# # ==========================================
#
# numbers = list(range(1, 11))
# result = list(
#     map(lambda x: x ** 2,
#         filter(lambda x: x % 2 == 0, numbers))
# )
#
# print("Q5 Output:")
# print(result)
# print()
#
#
# # ==========================================
# # Q6. Create your own version of map()
# # ==========================================
#
# def my_map(func, lst):
#     result = []
#     for item in lst:
#         result.append(func(item))
#     return result
#
# numbers = [1, 2, 3, 4, 5]
#
# print("Q6 Output:")
# print("my_map:", my_map(lambda x: x * 2, numbers))
# print("map   :", list(map(lambda x: x * 2, numbers)))
# print()
#
#
# # ==========================================
# # Q7. Find longest string using reduce()
# # ==========================================
#
# animals = ["cat", "elephant", "dog", "rhinoceros"]
#
# longest = reduce(
#     lambda a, b: a if len(a) > len(b) else b,
#     animals
# )
#
# print("Q7 Output:")
# print(longest)


def mystery(*args, **kwargs):
    print(sum(args), list(kwargs.values()))
mystery(1, 2, 3, a=4, b=5)

from functools import reduce
data = [2, 3, 4]
result = reduce(lambda a, b: a * b, list(map(lambda x: x + 1, data)))
print(result) 