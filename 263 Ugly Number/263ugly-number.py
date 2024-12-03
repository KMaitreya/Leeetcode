class Solution:
    def isUgly(self, n: int) -> bool:

        if n<=0:
            return False
        
        # def backtrack(total):

        #     if total==n:
        #         print(total)
        #         return True

        #     if total>n:
        #         return False

        #     for num in [2, 3, 5]:
        #         if backtrack(total*num):
        #             return True
        #     return False

        # return backtrack(1)


        for num in [2, 3, 5]:
            while n%num==0:
                n/=num

        if n==1:
            return True
        return False

        