# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
txt = input()
srch = input()
i=0
if re.search(srch,txt):
    while(i+len(srch)<=len(txt)):
        if(re.search(srch,txt[i:])):
            m = re.search(srch,txt[i:])
            print(f"({m.start()+i}, {i+m.end()-1})")
        i =i+m.start()+1
else: print("(-1, -1)")
        
