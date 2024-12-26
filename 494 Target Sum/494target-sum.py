class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        store={}
        n=len(nums)

        def backtrack(s, i):
            
            if (s, i) in store:
                return store[(s, i)]

            if i==n:
                if s==target:
                    return 1
                return 0
            store[(s, i)]=backtrack(s+nums[i], i+1)+backtrack(s-nums[i], i+1)
            return store[(s, i)]

        return backtrack(0, 0)