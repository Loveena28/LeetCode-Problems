class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSums = [0]*len(nums)
        runningSums[0] = nums[0]
        for i in range(1,len(nums)):
            runningSums[i] = runningSums[i-1] + nums[i]
        return runningSums
                
        