class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        val=3
        i=0
        p=pow(val, i)
        while p<=n:

            #print(val^i, val, i)
            if(p==n):
                return True
            i+=1

            p=pow(val, i)
        
        return False


            