from collections import deque
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = deque()
        for i in s:
            letters.append(i)
        for j in t:
            if j not in letters:
                return False
            letters.remove(j)
        return len(letters) == 0
            