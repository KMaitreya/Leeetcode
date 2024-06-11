class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        hmap={}
        op=[]

        for num in arr1:
            hmap[num]=hmap.get(num, 0)+1

        print(hmap)

        for num in arr2:
            op.extend([num]*hmap[num])
            del hmap[num]

        hmap=dict(sorted(hmap.items()))

        for key, value in hmap.items():
            op.extend([key]*value)

        del hmap

        return op