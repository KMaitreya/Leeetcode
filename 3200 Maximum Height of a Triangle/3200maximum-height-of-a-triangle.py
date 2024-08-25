class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        # total=0
        # i=1
        # rb=red+blue

        # while total<=rb:
        #     print(total, i)
        #     total+=i

        #     if total==rb:
        #         return i
        #     elif total>rb:
        #         return i-1
        #     i+=1


        ans =0
        b1,b2, r1,r2 =0,0,0,0
        for i in range(1, 10**10):
            if i%2==0:
                b1+=i
                r2+=i
            else:
                b2 +=i
                r1 +=i

            if (blue >= b1  and red >= r1) or (blue >= b2  and red >= r2):
                ans =i
            else:
                return ans
            
        