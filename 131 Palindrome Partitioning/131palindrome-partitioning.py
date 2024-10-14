class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]
        sub=[]
        n=len(s)

        def backtrack(i):
            if i>=n:
                res.append(sub.copy())
                return

            #loop
            for j in range(i, n):
                temp=s[i:j+1]
                if temp==temp[::-1]:
                    sub.append(temp)
                    backtrack(j+1)
                    sub.pop()

        backtrack(0)

        return res