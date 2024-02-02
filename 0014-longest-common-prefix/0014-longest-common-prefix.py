class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort()
        left,right = strs[0],strs[-1]
        for i in range(min(len(left),len(right))):
            if left[i]!=right[i]:
                return ans
            ans = ans + left[i]
        return ans
        