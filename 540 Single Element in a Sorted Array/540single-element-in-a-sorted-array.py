class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        cnt=1
        n=len(nums)

        if n==1:
            return nums[0]

        for i in range(n-1):
            if nums[i]==nums[i+1]:
                cnt+=1
            else:
                if cnt==1:
                    return nums[i]
                cnt=1

        return nums[-1]