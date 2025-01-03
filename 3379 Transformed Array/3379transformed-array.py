class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        res=[]
        nums+=nums+nums

        for i in range(n):
            res.append(nums[i+n+(nums[i+n]%n)])

        return res

        
