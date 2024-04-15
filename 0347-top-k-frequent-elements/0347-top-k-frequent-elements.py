class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in sorted(nums):
            count[i] = count.get(i,0) + 1
        ans = []
        count = dict(sorted(count.items(),key=lambda count:-count[1]))
        ans = [x for x in count.keys()][:k]
        return ans
        
        