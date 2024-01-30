class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for i in nums:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count_dict[i] = count_dict[i] + 1
        return len(list(filter(lambda x: count_dict[x]>1,count_dict))) != 0
        