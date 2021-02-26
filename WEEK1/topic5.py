from math import *
#####1
def A():
    n = float(input())
    print(n-int(n))



######2
def E():
    h=int(input())
    m=int(input())
    s=int(input())
    print(h * 30 + m * 30 / 60 + s * 30 / 3600)
######3
def H():
    p = int(input())
    x = int(input())
    y = int(input())
    x=x+x*(p/100)
    y=y+y*(p/100)
    x+=y//100
    y=y%100
    y+=((x-floor(x))*100)
    x=int(x)
    print(f"{x} {ceil(y)}")
######4
def O():
    n=int(input())
    x = float(input())
    count=1
    for i in range(n):
        count+=x**(i+1)
    print(count)
#####5

def M():
    n = int(input())
    count=1
    i=1
    while(i<n):
        count+=1/((i+1)**(2))
        i+=1
    print(f"{count:04f}")
M()