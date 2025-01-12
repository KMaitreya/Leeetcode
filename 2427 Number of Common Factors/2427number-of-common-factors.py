class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        l=min(a, b)
        cnt=1

        for i in range(2, l+1):
            if a%i==0 and b%i==0:
                cnt+=1

        return cnt