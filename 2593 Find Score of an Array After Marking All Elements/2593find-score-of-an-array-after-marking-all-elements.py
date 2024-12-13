class Solution:
    def findScore(self, nums: List[int]) -> int:

        visited=set()
        n=len(nums)
        vn=0
        res=0
        
        for i in range(n):
            nums[i]=(nums[i], i)

        heapq.heapify(nums)

        while vn<n:
            val, i=heapq.heappop(nums)

            if i not in visited:
                res+=val
                visited.add(i)
                vn+=1
            
                if i+1<=n-1:
                    if i+1 not in visited:
                        visited.add(i+1)
                        vn+=1

                if i-1>=0:
                    if i-1 not in visited:
                        visited.add(i-1)
                        vn+=1

        return res

