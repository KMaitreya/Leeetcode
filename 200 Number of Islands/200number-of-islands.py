class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        r, c=len(grid), len(grid[0])
        queue=[]
        v=set()
        cnt=0

        def bfs(a, b):
            q=[]
            q.append([a, b])
            v.add((a, b))

            while q:
                m, n=q.pop(0)
                if m+1<r and grid[m+1][n]=="1" and (m+1, n) not in v:
                    q.append([m+1, n])
                    v.add((m+1, n))
                if n+1<c and grid[m][n+1]=="1" and (m, n+1) not in v:
                    q.append([m, n+1])
                    v.add((m, n+1))
                if m-1>=0 and grid[m-1][n]=="1" and (m-1, n) not in v:
                    q.append([m-1, n])
                    v.add((m-1, n))
                if n-1>=0 and grid[m][n-1]=="1" and (m, n-1) not in v:
                    q.append([m, n-1])
                    v.add((m, n-1))
                

        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1" and (i, j) not in v:
                    print(i, j)
                    bfs(i, j)
                    cnt+=1

        return cnt
                



