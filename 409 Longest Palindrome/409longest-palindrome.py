class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        dic={}


        for char in s:
            if char in dic.keys():
                dic[char]+=1
            else:
                dic[char]=1

        cnt=0
        odd_cnt=0

        for key, value in dic.items():
            if value%2==0:
                cnt+=value
            else:
                cnt+=value-1
                odd_cnt=1

        return cnt+odd_cnt


        