class Solution:
    def longestPalindrome(self, s: str) -> str:

        n=len(s)
        l=0
        res=""

        for i in range(n):
            a, b=i, i
            while a>=0 and b<n and s[a]==s[b]:
                if (b-a+1)>l:
                    l=b-a+1
                    res=s[a:b+1]
                    print(l, res)
                a-=1
                b+=1

            a, b=i, i+1
            while a>=0 and b<n and s[a]==s[b]:
                if (b-a+1)>l:
                    l=b-a+1
                    res=s[a:b+1]
                    print(l, res)
                a-=1
                b+=1

        return res

