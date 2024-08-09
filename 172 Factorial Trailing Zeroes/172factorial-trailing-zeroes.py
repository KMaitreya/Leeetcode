class Solution:
    def trailingZeroes(self, n: int) -> int:

        s=1
        cnt=0
        
        for i in range(2, n+1):
            s*=i

        while s>10:
            if s%10==0:
                cnt+=1
                s=s//10
            else:
                break

        return cnt
