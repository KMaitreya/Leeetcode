class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        pre=[]
        temp=0

        for a in arr:
            temp^=a
            pre.append(temp)

        return [(pre[query[1]] if query[0]==0 else pre[query[1]]^pre[query[0]-1]) for query in queries]
