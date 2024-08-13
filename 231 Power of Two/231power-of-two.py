class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        return n>0 and n& (n-1)==0
        
        return int(math.log(n)/math.log(2))==math.log(n)/math.log(2)