class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        mcnt=0
        r, c=len(grid), len(grid[0])
        v=set()
        
        def bfs(a, b):

            q=[]
            cnt=1
            q.append((a, b))
            v.add((a, b))

            while q:
                m, n=q.pop(0)
                directions=[(0, 1), (1, 0), (0, -1), (-1, 0)]
                for d1, d2 in directions:
                    m1=m+d1
                    n1=n+d2
                    if m1 in range(r) and n1 in range(c) and (m1, n1) not in v and grid[m1][n1]==1:
                        q.append((m1, n1))
                        v.add((m1, n1))
                        cnt+=1
            return cnt

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1 and (i, j) not in v:
                    mcnt=max(mcnt, bfs(i, j))
        return mcnt
