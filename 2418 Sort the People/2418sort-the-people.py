class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        hmap={}
        op=[]

        for i in range(len(heights)):
            if heights[i] not in hmap.keys():
                hmap[heights[i]]=names[i]

        for key in sorted(hmap.keys()):
            op.append(hmap[key])

        return op[::-1]