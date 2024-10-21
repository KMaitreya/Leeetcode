class Solution:
    def climbStairs(self, n: int) -> int:
        
        ### BACKTRACKING-> ends with TLE
        
        # res=0

        # def backtrack(s):
        #     nonlocal res
        #     if s==n:
        #         res+=1
        #         return
            
        #     if s>n:
        #         return

        #     backtrack(s+1)
        #     backtrack(s+2)

        # backtrack(0)
        
        # return res

        ### DYNAMIC PROGRAMMING

        one=1
        two=1

        for i in range(n-1):
            one, two=one+two, one

        return one
            