class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        mapped={}

        for num in nums:
            s=""
            for digit in str(num):
                s+=str(mapping[int(digit)])
            s=int(s)
            if s in mapped.keys():
                mapped[s].append(num)
            else:
                mapped[s]=[num]

        nums=[]

        for key, value in sorted(mapped.items()):
            nums+=value

        return nums

