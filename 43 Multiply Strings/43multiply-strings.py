class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        n1, n2=0, 0

        l1=len(num1)
        l2=len(num2)
        
        for i in range(l1):
            n1+=(ord(num1[i])-48)*10**(l1-i-1)


        for i in range(l2):
            n2+=(ord(num2[i])-48)*10**(l2-i-1)


        return str(n1*n2)
