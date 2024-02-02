class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict = {}
        for i in s:
            count_dict[i] = 1 if i not in count_dict else count_dict[i] + 1
        new = dict(sorted(count_dict.items(),key = lambda x : x[1],reverse=True))
        ans = ""
        for key,value in new.items():
            ans = ans + "".join(key*value)
        return ans
        