from math import *
def hypotenuse():
    a = int(input())
    b = int(input())
    a = a**2
    b = b**2
    c = sqrt(a+b)
    print(c)


######2
def last_digit():
    a=int(input())
    a= a%10
    print(a)

#####3

def time2():
    n = int(input())
    s = n%60
    n //=60
    m = n%60
    n//=60
    print(f'{n:02d}:{m:02d}:{s:02d}')


####4

def pirozhki():
    a = int(input())
    c = int(input())
    k = int(input())

    c*=k
    a*=k
    a+=c//100
    c=c%100
    print(f"{a} {c}")


###5

def symetric():
    a = int(input())
    res = a%10*10+a//10%10-a//100 +1
    print(res)

symetric()