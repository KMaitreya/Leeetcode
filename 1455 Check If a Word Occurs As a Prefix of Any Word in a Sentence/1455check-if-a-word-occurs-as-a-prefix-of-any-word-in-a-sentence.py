class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence=sentence.split()
        l=len(searchWord)

        for i in range(len(sentence)):
            if sentence[i][:l]==searchWord:
                return i+1
        
        return -1