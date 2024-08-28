class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        op=[]
        
        for num in range(left, right+1):
            flg=True
            for digit in str(num):
                if digit is not '0':
                    if num%int(digit)!=0:
                        flg=False
                else:
                    flg=False
            if flg:
                op.append(num)

        return op