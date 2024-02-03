class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l=len(nums)
        cnt=0
        for i in range(l):
            if nums[i]==val:
                nums[i]=0
                cnt+=1
        nums.sort(reverse=True)
        return l-cnt
        