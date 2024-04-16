class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            count = [0] *26
            for j in i:
                count[ord(j) - ord('a')] = count[ord(j) - ord('a')] + 1
            ans[tuple(count)] = ans.get(tuple(count),[]) + [i]
        return list(ans.values())
        
        