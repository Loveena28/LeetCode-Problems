class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        for i in range(1,len(height)):
            max_left[i] = max(max_left[i-1],height[i-1])
        max_right = [0] * len(height)
        for i in range(len(height)-2,-1,-1):
            max_right[i] = max(max_right[i+1],height[i+1])
        
        res = 0
        for i in range(len(height)):
            water_level = min(max_left[i],max_right[i])
            if water_level >= height[i]:
                res += water_level - height[i]
        return res