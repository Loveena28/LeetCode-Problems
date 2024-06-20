from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = deque()
        queue.append((beginWord,1))
        
        if endWord not in wordSet:
            return 0
        
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        
        while queue:
            word,length = queue.popleft()
            for i in range(len(word)):
                new_letter = 'abcdefghijklmnopqrstuvwxyz'
                for c in new_letter:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word == endWord:
                        return length + 1
                    elif new_word in wordSet:
                        queue.append((new_word,length+1))
                        wordSet.remove(new_word)
        return 0