class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        i=num1.index("+")
        j=num2.index("+")

        return str(int(num1[:i])*int(num2[:j])-int(num1[i+1:-1])*int(num2[j+1:-1]))+"+"+str(int(num1[:i])*int(num2[j+1:-1])+int(num2[:j])*int(num1[i+1:-1]))+"i"

 