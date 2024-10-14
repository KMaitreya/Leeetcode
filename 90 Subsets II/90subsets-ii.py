class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        sub=[]
        n=len(nums)
        nums.sort()

        def backtrack(i):
            if i>=n:
                if sub not in res:
                    res.append(sub.copy())
                return

            sub.append(nums[i])
            backtrack(i+1)

            sub.pop()
            backtrack(i+1)


        backtrack(0)

        return res