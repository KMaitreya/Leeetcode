class Solution:
    def numTeams(self, rating: List[int]) -> int:

        # n=len(rating)

        # def counter(s):
        #     count=0

        #     for i in range(n):
        #         for j in range(i+1, n):
        #             for k in range(j+1, n):
        #                 if s[i]<s[j]<s[k]:
        #                     count+=1

        #     return count

        # return counter(rating)+counter(rating[::-1])

        n = len(rating)
        count = 0

        for j in range(n):
            left_smaller = left_larger = right_smaller = right_larger = 0

            # Count left smaller and larger
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                if rating[i] > rating[j]:
                    left_larger += 1

            # Count right smaller and larger
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                if rating[k] > rating[j]:
                    right_larger += 1

            # Calculate the number of valid teams
            count += left_smaller * right_larger + left_larger * right_smaller

        return count

        
        
