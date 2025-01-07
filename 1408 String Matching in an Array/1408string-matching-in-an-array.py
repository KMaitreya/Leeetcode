class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        l=len(words)
        res=set()

        for i in range(l):
            for j in range(l):
                if i!=j and words[i] in words[j]:
                    res.add(words[i])

        return list(res)