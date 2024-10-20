class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        r, c=len(grid), len(grid[0])
        q=[]
        v=set()
        t=0
        fresh=0
        rotten=0

        def helper(x, y):
            nonlocal fresh
            if x not in range(r) or y not in range(c) or (x, y) in v or grid[x][y]!=1:
                return
            grid[x][y]=2
            q.append((x, y))
            v.add((x, y))
            fresh-=1

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    rotten+=1
                    q.append((i, j))
                    v.add((i, j))
        if fresh==0:
            return 0

        while q:
            t+=1
            for _ in range(len(q)):
                a, b=q.pop(0)
                helper(a+1, b)
                helper(a-1, b)
                helper(a, b+1)
                helper(a, b-1)

        return t-1 if fresh==0 else -1