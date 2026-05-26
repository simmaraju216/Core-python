#syntax
# lambda paramaters : return value

#ex:
"""k=lambda x,y:print(x+y)
k(23,56)"""
"""great=lambda a,b:print(a) if a>b else print(b)
great(10,20)"""
#__________________________________________
#_______HIGHER ORDER FUNCTIONS____________
"""
1.map 2. filter 3.reduce 4.sorted
1. map
syntax:
map(functional reference,iterative value)
without map function
l=[I,O,L,U]
m=[]
for i in range(len(l)):
   k=ord(l[i])
   m.append(k)

with map
#To convert charectors to it's ascii vals
l=[a,s,d,f,g]
m=list(map(ord,l))
"""
"""# lambdafun + map function
l=[1,2,3,4,5]
m=list(map(lambda x:x**3,l))
print(*m)"""

#without mapfun

"""m=list(map(lambda x,y,z:x+y+z,[1,2,3],[4,5,6],[7,8,9]))
print(m)
# it perform first iteration first x=1stval in first list,y=1stval in 2ndlist,z=firstval in 3rd list
# it perform 2nd iteration 2nd x=2ndval in first list,y=2ndval in 2ndlist,z=2ndval in 3rd list
# it perform 3rd iteration 3rd x=3rdval in first list,y=3rdval in 2ndlist,z=3rdval in 3rd list"""


"""# to convert charactor from list of numbers
l=[66,67,68,69,70]
m=list(map(lambda x:x+4,l))
k=list(map(chr,m))
print(*k)"""
"""
l=[[1,2],[3,4],[5,6]]
k=list(map(lambda x:x+[5],l)) # it uses new address to modify i mean new variable(k)
print(l)     # [[1, 2], [3, 4], [5, 6]]
print(k)     #[[1, 2, 5], [3, 4, 5], [5, 6, 5]]
m=list(map(lambda x:x.append(5),l))# here existed list (l) is modified
print(l)   #[[1, 2, 5], [3, 4, 5], [5, 6, 5]]
print(m)    #[None, None, None]

"""
"""#_______using map_________
l=[1,2,3,4,5,6,7,8]
m=list(map(lambda x:x%2==0,l))
print(m)  # [False, True, False, True, False, True, False, True]"""
#________filtre()__________________
"""l=[1,2,3,4,5,6,7,8]
m=list(filter(lambda x:x%2==0,l))
print(m) # [2, 4, 6, 8]
"""
"""l=[1,2,3,4,5,6,7,8]
m=list(filter(lambda x:x%2,l))
print(m)  #  [1, 3, 5, 7]
"""
"""l=[3,6,1,2,5,9,12,16]
m=list(filter(lambda x:x%3,l))
print(m) # [1, 2, 5, 16]"""

"""# to remove vowels from string
s="Hello"
m=list(filter(lambda x:x not in "AEIOUaeiou",s))
print(m) #['H', 'l', 'l']"""