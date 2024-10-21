class Solution:
    def rob(self, nums: List[int]) -> int:
        
        one=0
        two=0

        for n in nums:
            one, two=two, max(one+n, two)

        return max(one, two)  

