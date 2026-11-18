class Solution:
    def isValid(self, s: str) -> bool:
        res = True
        pila = []
        if(len(s) % 2 == 1 or (s[0] == ')' or s[0] == '}' or s[0] == ']')): res = False
        else:
            pila.append(s[0])
            for i in range(1, len(s)):
                if(s[i] == '(' or s[i] == '{' or s[i] == '['):
                    pila.append(s[i])
                elif((len(pila)>0) and ((s[i] == ')' and pila[-1] == '(') or (s[i] == ']' and pila[-1] == '[') or (s[i] == '}' and pila[-1] == '{'))):
                    pila.pop()
                else:
                    res = False
                    break
            if (len(pila) > 0): res = False
        return res

sol = Solution()
print(sol.isValid("()[]{}"))