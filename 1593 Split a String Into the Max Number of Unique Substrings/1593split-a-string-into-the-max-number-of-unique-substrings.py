class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        n=len(s)

        def backtrack(i, v):
            if i==n:
                return 0

            res=0
            for j in range(i, n):
                sub=s[i:j+1]
                if sub not in v:
                    v.append(sub)
                    res=max(1+backtrack(j+1, v), res)
                    v.pop()

            return res

        return backtrack(0, [])
