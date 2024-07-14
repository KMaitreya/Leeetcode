class Solution:
    def getSmallestString(self, s: str) -> str:

        s=list(s)
        s1=""
        n=len(s)
        
        for i in range(n-1):
            a=int(s[i])
            b=int(s[i+1])
            if (a+b)%2==0 and b<a:
                s[i], s[i+1]=s[i+1], s[i]
                break
        
        for i in range(n):
            s1+=s[i]

        return s1