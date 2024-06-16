class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=list(s)
        op=[]

        for i in range(len(s)):
            if s[i].isalnum():
                op.append(s[i].lower())

        return op==op[::-1]