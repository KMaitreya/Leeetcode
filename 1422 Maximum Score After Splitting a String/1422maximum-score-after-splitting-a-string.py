class Solution:
    def maxScore(self, s: str) -> int:
        
        prefix=[int(s[0])]
        l=len(s)

        for i in range(1, l):
            prefix.append(prefix[-1]+int(s[i]))

        one=prefix[-1]
        mscore=0

        for i in range(1, l):
            mscore=max(mscore, one+i-2*prefix[i-1])

        return mscore

        