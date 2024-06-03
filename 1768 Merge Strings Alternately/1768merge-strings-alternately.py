class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)

        if l1>l2:
            n=l1
        else:
            n=l2

        merged=""

        for i in range(n):
            if i<l1:
                merged+=word1[i]
            if i<l2:
                merged+=word2[i]

            
        return merged
        