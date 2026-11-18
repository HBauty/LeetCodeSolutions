class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        pref = ""
        cambiar = True
        if(len(strs)>0):
          for i in range(len(strs[0])):
              pref += strs[0][i]
              for j in range(len(strs)):
                  if(not strs[j].startswith(pref)):
                      cambiar = False
                      break
              if(cambiar):
                  res = pref
              else:
                  return res
          return res

sol = Solution()
print(sol.longestCommonPrefix([""]))
