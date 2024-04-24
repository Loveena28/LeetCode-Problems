class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT,stackInd = stack.pop()
                res[stackInd] = index - stackInd
            stack.append([t,index])
        return res