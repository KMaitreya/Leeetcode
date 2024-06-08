class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        l1=len(haystack)
        l2=len(needle)
        i=0
        
        while i<=l1-l2:
            if needle==haystack[i:i+l2]:
                return i
            i+=1

        return -1
