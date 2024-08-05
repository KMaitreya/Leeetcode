class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        hmap={}
        cnt=0
        
        for char in arr:
            if char in hmap.keys():
                hmap[char]+=1
            else:
                hmap[char]=1

        for key, value in hmap.items():
            if value==1:
                cnt+=1
            if cnt==k:
                return key

        return ""