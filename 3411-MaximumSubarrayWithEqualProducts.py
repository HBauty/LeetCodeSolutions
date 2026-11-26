import math
from collections import deque
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        l,g = deque(),deque()
        prod = 1
        left = 0
        best = 0

        for right,num in enumerate(nums):
            prod *= num
            l.append(num)
            g.append(num)
            value = math.lcm(*l)*math.gcd(*g)
            while prod > value:
                prod = prod//nums[left]
                left += 1
                l.popleft()
                g.popleft()

            if prod == value:
                best = max(best,right-left+1)


        return best
