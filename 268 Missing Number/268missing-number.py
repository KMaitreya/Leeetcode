class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        flag=0
        length=len(nums)
        for i in range(length):
            if i!=nums[i]:
                flag=1
                break

        if flag==0:
            return length

        return i


        

        