#####1
def A():
    a = int(input())
    n = (int(input()))
    while(a<n):
        print(a)
        a+=1
######2
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
def G():

    n = int(input())
    k = int(input())
    sum = factorial(n)/(factorial(k)*factorial(n-k))
    print(sum)

######3
def N():
    n = int(input())
    count=0
    for i in range(n):
        a = int(input())
        if a==0:
            count+=1
    print(count)
#####4
def M():
    n = int(input())
    count=0
    for i in range(n):
        a = int(input())
        count+=a
    print(count)


###5
def T():
    n=int(input())
    count=0
    k=10
    for i in range(n):
        count+=(i+1)
        print(count)
        count*=k


T()