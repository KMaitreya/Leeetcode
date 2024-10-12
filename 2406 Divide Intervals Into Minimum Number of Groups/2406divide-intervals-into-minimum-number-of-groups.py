class Solution:
    import heapq
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        ### PArtially working solution

        # n=len(intervals)

        # cnt=0
        # mcnt=1

        # start={}
        # end={}

        # for x in intervals:
        #     start[x[0]]=1+start.get(x[0], 0)
        #     end[x[1]]=1+end.get(x[1], 0)

        # s=min(start.keys())
        # e=max(end.keys())

        # for i in range(s, e+1):
        #     if i in start.keys():
        #         cnt+=start[i]
        #     if i in end.keys():
        #         cnt-=end[i]
        #     mcnt=max(cnt, mcnt)

        # return mcnt

        ### Neetcode 2 pointer solution

        start, end=[], []

        for l, r in intervals:
            start.append(l)
            end.append(r)

        start.sort()
        end.sort()

        i=j=res=0

        for i in range(len(intervals)):
            if start[i]<=end[j]:
                i+=1
            else:
                j+=1
            res=max(res, i-j)

        return res