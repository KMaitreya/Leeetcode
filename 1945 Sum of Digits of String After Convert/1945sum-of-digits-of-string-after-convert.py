class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        num=""
        x=0
        s=s.upper()

        for char in s:
            num+=str(ord(char)-64)

        for i in range(k):
            for n in num:
                x+=int(n)
            num=str(x)
            x=0

        return int(num)