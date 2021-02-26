def A():
    s = input()
    print(s[2])
    print(s[-2])
    print(s[:5])
    print(s[:-2])
    print(s[::2])
    print(s[1::2])
    print(s[::-1])
    print(s[::-2])
    print(len(s))

def B():
    txt = input()
    print(txt.count(" "))

def C():
    txt = input()
    print(txt[(len(txt) + 1) // 2:] + txt[:(len(txt) + 1) // 2])

def E():
    txt = input()
    f=-1
    l=-1
    for i in range(len(txt)):
        if 'f' == txt[i] and f==-1:
            f=i
            l=i
        elif 'f' == txt[i]:
            l = i
    
    if f==l:
        print(f)
    else: print(f"{f} {l}")

def G():
    txt = input()
    f=-1
    l=-1
    for i in range(len(txt)):
        if 'h' == txt[i] and f==-1:
            f=i
            l=i
        elif 'h' == txt[i]:
            l =i
    res = txt[:f]+txt[l+1:]
    print(res)
