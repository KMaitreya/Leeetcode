class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap={}
        res=[]

        for num in nums:
            hmap[num]=hmap.get(num, 0)+1

        hmap=sorted(hmap, key=hmap.get, reverse=True)

        for i, key in zip(range(k), hmap):
            res.append(key)

        return res