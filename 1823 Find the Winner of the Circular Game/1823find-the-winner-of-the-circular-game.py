class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        queue=[]
        cnt=1
        
        for i in range(n):
            queue.append(i+1)

        while len(queue)!=1:
            if cnt==k:
                cnt=0
                del queue[0]
            else:
                queue.append(queue[0])
                del queue[0]
            cnt+=1

        return queue[0]
            
