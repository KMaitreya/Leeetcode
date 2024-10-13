class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        subset=[]
        n=len(nums)

        def backtrack(i):
            if i>=n:
                res.append(subset.copy())
                return

            #include nums[i]
            subset.append(nums[i])
            backtrack(i+1)

            #exclude nums[i]
            subset.pop()
            backtrack(i+1)

        
        backtrack(0)
        return res

