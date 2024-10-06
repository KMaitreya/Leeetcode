class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        # s1=sentence1.split()
        # s2=sentence2.split()
        # cnt=0

        # if len(s1)>len(s2):
        #     s1, s2=s2, s1
        
        # for word in s1:
        #     if word in s2:
        #         cnt+=1

        # return cnt==len(s1)

        s1 = sentence1.split()
        s2 = sentence2.split()

        # Ensure s1 is always the shorter or equal-length sentence
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        
        # Find the longest prefix match
        i = 0
        while i < len(s1) and s1[i] == s2[i]:
            i += 1
        
        # Find the longest suffix match
        j = 0
        while j < len(s1) - i and s1[len(s1) - 1 - j] == s2[len(s2) - 1 - j]:
            j += 1
        
        # Check if all words in s1 were matched either in the prefix or suffix
        return i + j == len(s1)
