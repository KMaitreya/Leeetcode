class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        cnt=0
        op=str(bin(start^goal))

        for num in op:
            if num=='1':
                cnt+=1

        return cnt
        

        