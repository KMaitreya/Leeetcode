class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s=="":
            return True
        
        if t=="":
            return False
        
        cnt=0
        i=0
        l=len(s)
        for char in t:
            if s[i]==char:
                cnt+=1
                i+=1
            if cnt==l:
                return True
        return False