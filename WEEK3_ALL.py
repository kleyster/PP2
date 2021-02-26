def A():
    arr = "".split(" ")

    for i in range(len(arr)):
        print(arr[2*i])


def B():
    arr = "".split(" ")

    min = 1000
    for i in arr:
        if min>i and i>0:
            min = i
def C():
    arr = [1,2,3,4,5]
    print(arr[::-1])


def D():
    arr = [4,0,5,0,3,0,0,5]

    for i in arr:
        if i!=0:
            print(i,end=" ")
    for i in range(arr.count(0)):
        print(0,end=" ")

def E():
    arr = "".split(" ")

    arr = [5,3,7,4,6]
    k = 3
    print(arr[-k:], end=' ')
    print(arr[0:-k])

def F():
    arr = "1 2 3 4 5 6 7 8 9 10".split(" ")
    origin =[]
    for i in arr:
        if not (i in origin):
            origin.append(i)
    print(len(origin))

def G():
    arr1 = "".split(" ")
    arr2 = "".split(" ")
    orr=[]
    for i in arr1:
        if i in arr2:
            orr.append(i)
    print(len(orr))

def H():
    arr1 = "".split(" ")
    arr2 = "".split(" ")
    orr = []
    for i in arr1:
        if i in arr2:
            orr.append(i)
    for i in orr:
        print(i,end=" ")

def I():
    n = int(input())
    m = int(input())
    arr1=[]
    arr2 = []
    arr3=[]
    for i in range(len(n)):
        arr1.append(int(input()))
    for i in range(len(m)):
        arr2.append(int(input()))
    for i in arr1:
        if i in arr2:
            arr3.append(i)
            arr1.pop(i)
            arr2.pop(i)
    print(len(arr3))
    for i in arr3:
        print(i,end=" ")
    print(len(arr1))
    for i in arr1:
        print(i,end=" ")
    print(len(arr2))
    for i in arr2:
        print(i,end=" ")
    

def J():
    d = {}
    n = int(input())
    for i in range(n):
        s = input().split(" ")
        a = s[0]
        b = s[1]
        d[a]=b
        d[b]=a
    s = input()

    print(d.get(s))

def K():
    d = {}
    s = input().split(" ")
    max = 0
    for i in s:
        d[i] = d.get(i,0)+1
        if d[i]>max:
            max = d[i]
    
    d = [(v,k) for k,v in d.items()]
    d = sorted(d)
    for i in d[::-1]:
        print(i[1])
