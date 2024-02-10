class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s=s[::-1]
        l=len(s)
        cnt=0
        for i in range(l):
            if s[i]!=' ':
                cnt+=1
            elif cnt==0:
                pass
            else:
                return cnt

        return cnt