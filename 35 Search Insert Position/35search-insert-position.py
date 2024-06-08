class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if len(nums)==1:
            if target>nums[0]:
                return 1
            else:
                return 0

        elif nums[0]>target:
            return 0

        elif nums[-1]<target:
            return len(nums)

        elif nums[-1]==target:
            return len(nums)-1
        

        for i in range(len(nums)-1):
            if nums[i]==target:
                return i
            if nums[i]<target and nums[i+1]>target:
                return i+1
            