"""def fun1(x,y):
   print(x,y)
   return x+y
def fun2(a,b):
    c=fun1(a,b)
    print(c*c)
fun2(10,20)"""

#_________________________________

"""def fun1(x,y):
   print(x,y)
   return x+y
def fun2(z,a,b):
    z(a,b)
fun2(fun1,10,20)"""

def fun():
    x=10
    y=50
    z=x+y
    def fun2():
        print(z)
        print("hi")
    return fun2
f=fun()
f()
