class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        l=len(nums)

        if l==1:
            return True
        
        for i in range(1,len(nums)):
            if (nums[i-1]+nums[i])%2==0:
                return False

        return True