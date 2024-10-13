class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # res=[]
        # sub=[]
        # n=len(nums)
        

        # def backtrack(i):

        #     if i>=n:
        #         return
            
        #     if len(sub)==n:
        #         res.append(sub.copy())
        #         return

        #     for i in range(n):
        #         if nums[i] not in sub:
        #             sub.append(nums[i])
        #             backtrack(i)
        #             sub.pop()

        # backtrack(0)

        # return res

        res=[]

        if len(nums)==1:
            return [nums.copy()]

        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)

        return res