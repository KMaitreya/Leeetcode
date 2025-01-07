class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        val=x
        harshad=0

        while x>0:
            harshad+=x%10
            x=x//10

        return harshad if val%harshad==0 else -1