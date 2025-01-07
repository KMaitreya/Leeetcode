class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        s=s.lower()
        cnt=0

        for i in range(1, len(s)):
            if s[i-1]!=s[i]:
                cnt+=1

        return cnt