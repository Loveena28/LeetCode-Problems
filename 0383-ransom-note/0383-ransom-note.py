class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charactersInRansom = {}
        for i in ransomNote:
            if i not in charactersInRansom:
                charactersInRansom[i] = 1
            else:
                charactersInRansom[i] = charactersInRansom[i] + 1
        for j in magazine:
            if j in charactersInRansom and charactersInRansom[j] > 0:
                charactersInRansom[j] = charactersInRansom[j] - 1
        return len(list(filter(lambda x : charactersInRansom[x] != 0,charactersInRansom))) == 0
            