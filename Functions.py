# Orbitary functions are 1. *args-positional in form of tuple
"""def fun1(*a):  #
    print(a)
    print(*a)
fun1(10,10,20,30,50,60)"""

"""def fun3(a,b,c,d):
    print(a,b,c,d)   2. **args-positional in form of dict
def fun2(**b):
    print(b)
    fun3(**b)
fun2(a=75,b=30,c=40,d=70)"""

"""def fun4(*a,**b):
    print(a,b,sep='\n')
fun4(10,1,2,3,45,6,b=11,a=50)"""

"""def fun6(*a):
    print(a)
   #print(sum(a))
    sum=0
    for i in a:
        if i%2==0:#if i&1==0:
            sum+=i
    print(sum)

fun6(1,7,8,25,30,60,70)"""

""""
def fun6(*a):
    print(a)
    sum1=0  #Alternative sum
    sum2=0
    for i in range(len(a)):
        if i%2==0:
            sum1+=a[i]
        else:
            sum2+=a[i]
    print(sum1)
    print(sum2)

fun6(1,2,3,4,5,7,7,8,8,10)  """
"""_____________or__________
def fun6(*a):
    print(a)
    print(sum(a[::2]))
    print(sum(a[1::2]))
fun6(1,2,3,4,5,7,7,8,8,10)"""