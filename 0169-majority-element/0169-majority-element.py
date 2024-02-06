class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for i in nums:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count_dict[i] = count_dict[i] + 1
        max_no = len(nums) / 2
        return list(filter(lambda x : count_dict[x] > max_no,count_dict))[0]
        