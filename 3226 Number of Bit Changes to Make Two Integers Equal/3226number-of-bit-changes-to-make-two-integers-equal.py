class Solution:
    def minChanges(self, n: int, k: int) -> int:
        
        nb=list(bin(n))[2:][::-1]
        kb=list(bin(k))[2:][::-1]

        l1=len(nb)
        l2=len(kb)

        cnt=0

        if l1>l2:
            kb.extend((l1-l2)*str(0))
        else:
            nb.extend((l2-l1)*str(0))

        for i in range(l1):
            if nb[i]=='1' and kb[i]=='0':
                nb[i]='0'
                cnt+=1
        
        if nb==kb:
            return cnt
        return -1

       
