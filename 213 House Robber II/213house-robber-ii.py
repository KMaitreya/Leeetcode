class Solution:
    def rob(self, nums: List[int]) -> int:
        
        one, two=0, 0
        n=len(nums)

        for i in range(1, n):
            one, two=two, max(one+nums[i], two)

        r1=max(one, two)

        one, two=0, 0

        for i in range(n-1):
            one, two=two, max(one+nums[i], two)

        r2=max(one, two)

        return max(nums[0], r1, r2)