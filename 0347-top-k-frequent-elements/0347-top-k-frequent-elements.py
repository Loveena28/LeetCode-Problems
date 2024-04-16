class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        finalAns = []
        tempArr = [[] for _ in range(len(nums) + 1)] 
        for i in sorted(nums):
            count[i] = count.get(i,0) + 1 # stores the frequency of each number
        for i in count:
            tempArr[count[i]].append(i) 
            # at every index, its list will be appended with the numbers whose frequency is equal to the index, TC = O(n)
        for i in range(len(tempArr)-1,0,-1):
            if not tempArr[i] or len(finalAns) >= k:
                continue
            for j in tempArr[i]:
                finalAns.append(j)
        return finalAns
        
        