class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend==0:
            return 0

        if divisor==1:
            return min(max(-2**31, dividend), 2**31-1)

        if divisor==-1:
            return min(max(-2**31, -dividend), 2**31-1)
        
        val=int(math.pow(8, math.log(abs(dividend), 8)-math.log(abs(divisor), 8)))

        if (dividend<0)^(divisor<0):
            val=-val

        return min(max(-2**31, val), 2**31-1)