class Solution:
    def findComplement(self, num: int) -> int:
        
        num=str(bin(num))
        bis=""

        for i in range(2,len(num)):
            if num[i]=="0":
                bis+="1"
            else:
                bis+="0"

        return int(bis, 2)