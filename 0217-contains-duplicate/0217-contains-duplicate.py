class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequencyNums = {}
        for i in nums:
            if i not in frequencyNums:
                frequencyNums[i] = 1
            else:
                frequencyNums[i] = frequencyNums[i] + 1
        return len(list(filter(lambda x : frequencyNums[x] > 1,frequencyNums))) > 0
        