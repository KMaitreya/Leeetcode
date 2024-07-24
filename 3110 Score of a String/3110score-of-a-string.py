class Solution:
    def scoreOfString(self, s: str) -> int:
        
        cnt=0
        for i in range(1,len(s)):
            cnt+=abs(ord(s[i-1])-ord(s[i]))

        return cnt