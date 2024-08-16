class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        mins, maxs=[], []
        
        for i in range(len(arrays)):
            mins.append((arrays[i][0], i))
            maxs.append((arrays[i][-1], i))

        mins.sort()
        maxs.sort()

        n=len(mins)
        m=len(maxs)

        i, j=0, m-1

        while i<n or j>0:
            if maxs[j][1]!=mins[i][1]:
                return abs(maxs[j][0]-mins[i][0])
            elif maxs[j][0]-maxs[j-1][0]>=mins[i+1][0]-mins[i][0]:
                i+=1
            else:
                j-=1