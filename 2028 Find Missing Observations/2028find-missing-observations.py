class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        return (n<=(p:=mean*(n+len(rolls))-sum(rolls))<=n*6)*(p%n*[p//n+1]+(n-p%n)*[p//n])

