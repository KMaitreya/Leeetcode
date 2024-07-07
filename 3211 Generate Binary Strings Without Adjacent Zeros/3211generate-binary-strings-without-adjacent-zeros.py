class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        i=0
        op=[]

        while i<2**n:
            b=format(i, f'0{n}b')
            if "00" in b:
                pass
            else:
                op.append(b)
            i+=1
            

        return op