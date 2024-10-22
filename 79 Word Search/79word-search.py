class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        r, c=len(board), len(board[0])
        v=[]

        # def helper(x, y, i, q):
        #     if i<len(word):
        #         if x in range(r) and y in range(c) and board[x][y]==word[i] and (x, y) not in v:
        #             q.append((x, y))
        #             v.append((x, y))
        #             i+=1

        # def dfs(s):
        #     n=len(word)
        #     for x in s:
        #         i=1
        #         q=[]
        #         q.append(x)
        #         while q:
        #             print(q)
        #             if i==n:
        #                 return True
        #             m, n=q.pop(0)
        #             res=helper(m+1, n, i, q) orhelper(m-1, n, i, q) or helper(m, n-1, i, q) or helper(m, n+1, i, q)
        #     return False

        def dfs(x, y, i):
            if i==len(word):
                return True
            if x not in range(r) or y not in range(c) or board[x][y]!=word[i] or (x, y) in v:
                return False

            v.append((x, y))
            res=dfs(x+1, y, i+1) or dfs(x-1, y, i+1) or dfs(x, y+1, i+1) or dfs(x, y-1, i+1)
            v.pop()
            return res


        for k in range(r):
            for j in range(c):
                if dfs(k, j, 0):
                    return True
        return False
