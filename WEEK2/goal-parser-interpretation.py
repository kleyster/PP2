class Solution:
    def interpret(self, command: str) -> str:
        s = ""
        for i in range(len(command)):
            if command[i]=="G":
                s+="G"
            elif command[i:i+2]=="()":
                s+="o"
            elif command[i:i+4]=="(al)":
                s+="al"
        return s