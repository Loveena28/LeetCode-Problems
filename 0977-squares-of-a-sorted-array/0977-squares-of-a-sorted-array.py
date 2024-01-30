class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = sorted([i**2 for i in nums])
        return new_list