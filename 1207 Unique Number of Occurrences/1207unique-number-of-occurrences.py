class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
    
        dic={}
        res=[]

        for num in arr:
            if num in dic.keys():
                dic[num]+=1
            else:
                dic[num]=1
            
        for key, value in dic.items():
            res.append(value)


        if len(res)==len(set(res)):
            return True
        return False
