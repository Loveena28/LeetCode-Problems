class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        temp_arr = list(range(n+1))
        return list(set(temp_arr) - set(nums))[0]
        