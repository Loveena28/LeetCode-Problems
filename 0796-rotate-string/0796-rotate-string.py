class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i = 0
        while i<len(s):
            if s == goal:
                return True
            s = s[1:] + s[0]
            i = i + 1

        return False   
        