class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        if c==0:
            return True

        i=1

        while i**2<c:
            s=(c-i**2)**0.5
            if int(s)==s:
                return True
            i+=1
        return False