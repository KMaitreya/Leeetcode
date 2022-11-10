class Solution:
    def reverse(self, x: int) -> int:

        flg=0
        s=""

        if x<0:
            flg=1

        x=abs(x)
        numstr=str(x)

        for i in numstr:
            s=i+s

        x=int(s)

        if x<-2147483648 or x>2147483647:
            return 0

        if flg==1:
            return x*-1
        
        return x
