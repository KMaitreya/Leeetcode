class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        # curr=1
        # prev=curr-1

        # for i in range(time):
        #     print(i, n, curr, prev)

        #     if curr>=1 and curr<n and curr>prev:
        #         print("if")
        #         prev=curr
        #         curr+=1
        #     else:
        #         print("elif")
        #         prev=curr
        #         curr-=1
        #     curr=abs(curr)

        # return curr

        # l,s=[],[]

        # print(time//n)

        # for i in range(1, n):
        #     s.append(i)

        # for i in range(n, 1, -1):
        #     s.append(i)

        # for i in range(time//n):
        #     l.extend(s)

        # print(l[time])

        pos, direction=1, 1

        for i in range(time):
            pos+=direction
            if pos==n:
                direction=-1
            elif pos==1:
                direction=1

        return pos


        

        return 0