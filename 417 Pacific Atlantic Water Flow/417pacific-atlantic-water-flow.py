class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        r, c=len(heights), len(heights[0])
        vp=set()
        va=set()
        q=[]


        def helper(x, y, val, arr):
            if x in range(r) and y in range(c) and heights[x][y]>=val and (x, y) not in arr:
                arr.add((x, y))
                q.append((x, y))


        def dfs(a, b, arr):
            q.append((a, b))
            while q:
                m, n=q.pop()
                helper(m+1, n, heights[m][n], arr)
                helper(m-1, n, heights[m][n], arr)
                helper(m, n+1, heights[m][n], arr)
                helper(m, n-1, heights[m][n], arr)
            

        #Pacific ocean

        for j in range(c):
            vp.add((0, j))
            dfs(0, j, vp)

        for i in range(r):
            vp.add((i, 0))
            dfs(i, 0, vp)

        #Atlantic ocean

        for j in range(c):
            va.add((r-1, j))
            dfs(r-1, j, va)

        for i in range(r):
            va.add((i, c-1))
            dfs(i, c-1, va)

        return list(vp & va)