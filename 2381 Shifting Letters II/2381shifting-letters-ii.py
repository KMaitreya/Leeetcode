class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        letters=string.ascii_lowercase

        hmap={letters[i]: i for i in range(26)}

        s=list(s)
        l=len(s)
        final=[0]*l

        for st, e, direction in shifts:
            if direction==0:
                final[st]-=1
                if e+1<l:
                    final[e+1]+=1
            else:
                final[st]+=1
                if e+1<l:
                    final[e+1]-=1
        
        s[0]=letters[(hmap[s[0]]+final[0])%26]

        for i in range(1,l):
            final[i]+=final[i-1]
            s[i]=letters[(hmap[s[i]]+final[i])%26]

        return "".join(s)


        