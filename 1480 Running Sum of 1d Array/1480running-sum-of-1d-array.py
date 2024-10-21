class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        x=0
        op=[]

        for num in nums:
            x+=num
            op.append(x)

        return op