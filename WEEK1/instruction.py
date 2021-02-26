def A():
    a = int(input())
    b = int(input())
    if(a>b):
        print(a)
    else: print(b)

### 2
def G():
    a= int(input())
    b= int(input())
    c= int(input())
    count=0
    if (a==b):
        count+=1
    elif(b==c):
        count+=1
    elif(a==c):
        count+=1
####3
def Q():
    n = int(input())
    if n==1:
        print(f"1 korova")
    elif n>=2 and n<=4:
        print(f"{n} korovy")
    else:
        print(f"{n} korov")

######4
def S():
    a = int(input())
    b= int(input())
    c = int(input())
    m=max(max(a,b),c)
    if m==a:
        m1=b
        m2=c
    elif m==b:
        m1=a
        m2=c
    else:
        m1=a
        m2=b

    if(m1+m2>m):
        if(m1**2+m2**2==m**2):
            print("rectangular")
        elif(m1**2+m2**2>m**2):
            print("acute")
        else:
            print("obtuse")
    else:
        print("imposible")
####5
def F():
    a = int(input())
    b= int(input())
    c = int(input())
    if(a+b>c):
        print("YES")
    else: print("NO")