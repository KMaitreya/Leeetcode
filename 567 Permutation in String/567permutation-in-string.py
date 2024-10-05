class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False

        s1=list(s1)
        s2=list(s2)
        
        s1.sort()

        l1=len(s1)

        for i in range(len(s2)-l1+1):
            if s1==sorted(s2[i:i+l1]):
                return True
        return False
                