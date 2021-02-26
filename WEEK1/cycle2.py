def A():
    n = int(input())
    i=1
    while(True):
        sq = i**2
        if sq>n:
            break
        else:
            print(sq)

def D():
    n=int(input())
    while(n>1):
        if n%2!=0:
            print("NO")
            return
        n/=2
    print("YES")

def F():
    n = int(input())
    k = int(input())
    i=1
    while(n<k):
        n=n+n*(0.1)
        i+=1
    print(i)

def L():
    sum=0
    while(True):
        n=int(input())
        if(n==0):
            print(sum)
            return
        sum+=n
    
def I():
    sum=0
    while(True):
        n=int(input())
        if(n==0):
            print(sum)
            return
        sum+=n

def J():
    sum=0
    i=1
    while(True):
        n=int(input())
        if(n==0):
            print(sum/i)
            return
        sum+=n
        i+=1