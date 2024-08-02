class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        ##### FIRST ATTEMPT

        # cnt=0
        # idx, jdx=0, 0
        
        # while True:

        #     for i in range(len(nums)-1, -1, -1):
        #         if nums[i]==0:
        #             idx=i
        #             break

        #     for j in range(len(nums)):
        #         if nums[j]==1:
        #             jdx=j
        #             break

        #     print(idx, jdx, nums)

        #     nums[idx], nums[jdx]=nums[jdx], nums[idx]
        #     cnt+=1

        #     if idx<jdx:
        #         return cnt


        #### SECOND ATTEMPT

        # n, mcnt=0, 99999

        # for num in nums:
        #     if num==1:
        #         n+=1

        # nums=nums+nums[:n]

        # for i in range(len(nums)-n):
        #     cnt=0
        #     for j in range(n):
        #         if nums[j+i]!=1:
        #             cnt+=1
        #     if cnt<mcnt:
        #         mcnt=cnt

        
        # return mcnt


        #### THIRD ATTEMPT

        n, cnt, mcnt=0, 0, 99999

        for num in nums:
            if num==1:
                n+=1

        for i in range(n):
            if nums[i]==0:
                cnt+=1

        nums+=nums[:n]

        for i in range(len(nums)-n):
            
            if nums[i]==0:
                cnt-=1
            if nums[i+n]==0:
                cnt+=1

            if cnt<mcnt:
                mcnt=cnt

        return mcnt