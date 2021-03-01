# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    k = input()
    if(re.search(r'[7-9]\d{9}',k) and len(k)==10):
        print("YES")
    else:
        print("NO")
