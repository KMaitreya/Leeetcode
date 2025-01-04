class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        cnt=0
        visited=set()

        for c in s:
            if c not in visited:
                visited.add(c)
                l=s.index(c)
                r=s.rindex(c)
                if l<r:
                    cnt+=len(set(s[l+1:r]))

        return cnt
            