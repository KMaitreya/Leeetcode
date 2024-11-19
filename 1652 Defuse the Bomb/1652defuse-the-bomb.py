class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        n=len(code)

        if k==0:
            return [0]*n

        code+=code

        # if k<0:
        #     s=sum(code[k-1:-1])
        #     print(s, code[k-1:-1])
        #     res.append(s)
        #     for i in range(n-2, -1, -1):
        #         print(s, code[i], code[i-1], code[i-k-1])
        #         res.insert(0, s-code[i-1]+code[i-k-1])
        #     return res
        # else:
        #     s=sum(code[1:k+1])
        #     res.append(s)
        #     for i in range(1, n):
        #         res.append(s-(i-1)+(i+k+1))
        #     return res

        if k<=0:
            code=code[::-1]
            return [sum(code[i+1:i-k+1]) for i in range(n)][::-1]
        return [sum(code[i+1:i+k+1]) for i in range(n)]
        
