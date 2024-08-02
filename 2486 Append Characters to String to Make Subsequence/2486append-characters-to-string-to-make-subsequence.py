class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        sl=len(s)
        tl=len(t)

        i, j=0, 0

        cnt=0

        if tl==1 and t[0] in s:
            return 0
        
        while i<sl:
            if t[j]==s[i]:
                cnt+=1
                j+=1
            else:
                j=cnt
            i+=1

        return tl-cnt