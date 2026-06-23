# To print prime using function
def prime(n):
    if n==1:
        return'not prime'
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return'not a prime'
        else:
            return 'prime'
n=int(input())
p=prime(n) # copy of a function
print(p)
# TO print  Factorial of a number
def fact(a):
    f=1
    for i in range(a,0,-1):
        f=f*i
    print(f)
a=int(input())
fact(a)

# TO print n number of  Factorial of a numbers
def n_fact(a):
    for j in range(a+1):
        f=1
        for i in range(j,0,-1):
            f=f*i
        print(f,end=' ')
a=int(input())
n_fact(a)

def feb(n):
    a,b=0,1
    for i in  range(n):
        c=a+b
        print(a)
        a=b
        b=c
n=int(input())
feb(n)

a=[1,2,3,4]
b=[10,20,30,40]
k=list(map(lambda x,y:x+y,a,b))
print(k)

l=[12,15,7,18,20,21,25]
k=list(filter(lambda x: (x%3==0)!=(x%5==0),l))
print(k)

from functools import reduce
l=[1,2,3,4]
m=reduce(lambda x,y:x*y,l)
print(m)

l=[[1,2],[3,4],[5,6]]
m=list(map(lambda sub:list(map(lambda x:x+5,sub)),l))
print(m)

from functools import reduce
l=[7,8,15,10]
k=reduce(lambda x,y:x if x>y else y,l)
print(k)

a=list(map(int,input().split()))
print(a)