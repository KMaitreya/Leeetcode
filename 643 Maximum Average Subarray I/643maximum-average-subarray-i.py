class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums)==1:
            return nums[0]

        s=sum(nums[0:k])
        m=s

        for i in range(len(nums)-k):
            s+=nums[i+k]-nums[i]
            if s>m:
                m=s
            

        return m/k