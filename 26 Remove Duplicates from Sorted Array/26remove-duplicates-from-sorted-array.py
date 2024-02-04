class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l=len(nums)
        num=[]
        k=1
        num.append(nums[0])
        for i in range(1,l):
            if nums[i]!=nums[i-1]:
                num.append(nums[i])
                k+=1
        nums[:k]=num
        return k