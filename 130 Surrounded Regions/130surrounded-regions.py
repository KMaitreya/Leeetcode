class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # r, c=len(board), len(board[0])
        # v=set()
        # q=[]
        # temp=[]

        # def helper(x, y):
        #     if x in range(1, r-1) and y in range(1, c-1) and (x, y) not in v and board[x][y]=="O":
        #         v.add((x, y))
        #         q.append((x, y))
        #         return True

        # def dfs(a, b):

        #     q.append((a, b))
        #     while q:
        #         (m, n)=q.pop(0)
        #         helper(m+1, n)
        #         helper(m-1, n)
        #         helper(m, n+1)
        #         helper(m, n-1)
        #     return


        # for i in range(1,r-1):
        #     for j in range(1, c-1):
        #         if (i, j) not in v and board[i][j]=="O":
        #             v.add((i, j))
        #             dfs(i, j)


        # for i, j in v:
        #     board[i][j]="X"

        r, c=len(board), len(board[0])
        v=[]
        q=[]

        def helper(x, y):
            if x in range(r) and y in range(c) and (x, y) not in v and board[x][y]=="O":
                q.append((x, y))
                v.append((x, y))
            return


        def dfs(a, b):
            q.append((a, b))
            while q:
                m, n=q.pop()
                helper(m+1, n)
                helper(m-1, n)
                helper(m, n+1)
                helper(m, n-1)


        for j in range(c):
            if board[0][j]=="O":
                v.append((0, j))
                dfs(0, j)

            if board[r-1][j]=="O":
                v.append((r-1, j))
                dfs(r-1, j)


        for i in range(1, r-1):
            if board[i][0]=="O":
                v.append((i, 0))
                dfs(i, 0)
                
            if board[i][c-1]=="O":
                v.append((i, c-1))
                dfs(i, c-1)

        for i in range(1, r-1):
            for j in range(1, c-1):
                if board[i][j]=="O" and (i, j) not in v:
                    board[i][j]="X"
