class Solution:
    def checkString(self, s: str) -> bool:
        i = 0
        res = True
        while i < len(s) and s[i] == 'a':
            i +=1
        while i < len(s) and s[i] == 'b':
            i +=1
        if(i < len(s) and s[i] != 'b'): res = False
        return res
