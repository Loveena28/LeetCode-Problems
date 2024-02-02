class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_dict = {}
        for i in s:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count_dict[i] = count_dict[i] + 1
        for j in t:
            if j in count_dict:
                count_dict[j] = count_dict[j] - 1
        return len(list(filter(lambda x : count_dict[x] != 0,count_dict))) == 0
        