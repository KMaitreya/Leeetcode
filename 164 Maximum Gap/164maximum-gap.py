class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums)<2:
            return 0

        temp, diff=0, 0

        nums=sorted(nums)

        for i in range(len(nums)-1):
            temp=nums[i+1]-nums[i]
            if temp>diff:
                diff=temp

        return diff