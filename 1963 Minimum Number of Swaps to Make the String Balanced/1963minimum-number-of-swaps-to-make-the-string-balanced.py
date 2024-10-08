class Solution:
    def minSwaps(self, s: str) -> int:

        e=0
        me=0

        for x in s:
            if x=="]":
                e+=1
            else:
                e-=1
            me=max(e, me)

        return (me+1)//2