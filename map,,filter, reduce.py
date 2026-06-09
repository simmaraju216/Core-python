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
#
# nums = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda x: x.append(10),nums))
# print("Result:", result)
# print("Nums:", nums)
#
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

l=['Hello','Hii','Who','are','you?']  #in"AEIOUaeiou"
m=list(map(lambda x:list(filter(lambda ch:ch not in "AEIOUaeiou",x)),l))
print(m)
l1=[]
for i in m:
    k=list(map(ord,i))
    l1.append(sum(k))
print(l1)
print(sum(l1))
"""_______________or_________________"""
# for i in l:
#     m=list(map(lambda x:x if x not in "AEIOUaeiou"else '',i))
#     print(m)