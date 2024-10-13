class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        res=[]
        n=len(candidates)

        def backtrack(i, sub):
            if sum(sub)==target:
                res.append(sub.copy())
                return
            
            if i>=n or sum(sub)>target:
                return

            #decision to add nums[i]
            sub.append(candidates[i])
            backtrack(i, sub)

            #decision to not add nums[i]
            sub.pop()
            backtrack(i+1, sub)

        backtrack(0, [])

        return res