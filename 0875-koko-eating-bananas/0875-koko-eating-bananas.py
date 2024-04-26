import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left,right = 1,max(piles)
        res = right
        while left <= right:
            mid = left + (right-left)//2
            time = sum([math.ceil(x/mid) for x in piles])
            if time <= h:
                right = mid-1
                res = min(res,mid)
            else:
                left = mid + 1
        return res