class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: # left sorted portion 
                if nums[mid] < target or nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # right sorted portion
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        