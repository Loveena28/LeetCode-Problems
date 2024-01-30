class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = list(range(1,len(nums)+1))
        return list(set(temp) - set(nums))
        