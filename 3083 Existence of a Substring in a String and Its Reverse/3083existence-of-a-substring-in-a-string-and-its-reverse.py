class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        
        sub=set()
        l=len(s)

        for i in range(l-1, 0, -1):
            sub.add(s[i]+s[i-1])

        for x in sub:
            if x in s:
                return True

        return False