# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())

for i in range(n):
    k = input()
    if(re.search(r"<[A-Za-z](\w|-|\.|_)+[@][A-Za-z]+\.[a-zA-Z]{1,3}>",k)):
        print(k)
