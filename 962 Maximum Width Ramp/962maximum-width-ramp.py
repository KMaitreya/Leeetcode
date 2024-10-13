class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        ### Sliding window/ two pointer approach
        n=len(nums)
        maxes=[0]*n
        prev=0

        for i in range(n-1, -1, -1):
            maxes[i]=max(prev, nums[i])
            prev=maxes[i]

        l=0
        res=0

        for r in range(1, n):
            while nums[l]>maxes[r]:
                l+=1
            res=max(res, r-l)

        return res
