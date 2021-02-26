####1

def calc_power(p):
    print(pow(2,p))

#####2
def fact(n):
    f = 1
    for i in range(n):
        f*=i
    print(f)

#######3
from math import *
def hypotenuza(a,b):
    a = a**2
    b = b**2
    c = sqrt(a+b)
    print(c)

####4
def leibniz():
    sum = 0
    for i in range(10):
        sum = sum + ((-1)**i)*(4/(2*i+1))
    print(sum)
###5
def zeta():
    sum = 0
    for i in range(10):
        sum=sum+(1/(i+1)**2)
    print(sum)


####6
def print_A():
    a='A'
    a = a*100
    print(a)

#####7
def python_print():
    p = "Python"
    p = p*100
    print(p)

#####8
def H():
    a = 179**10
    a = str(a)*4
    res = int(a)**(1/10)
    print(res)

#####9
def I():
    a = "179"*50
    a = int(a)**2
    print(a)
I()