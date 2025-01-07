class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        capacity.sort(reverse=True)
        total=sum(apple)
        s, i=0, 0

        while s<total:
            s+=capacity[i]
            i+=1

        return i