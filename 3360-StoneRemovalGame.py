class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        turn = 0
        while(n - stones >= 0 and stones > 0):
            n = n-stones
            stones = stones-1
            turn = turn + 1
        return (turn%2)!=0
