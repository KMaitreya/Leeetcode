class Solution:
    def isHappy(self, n: int) -> bool:

        visited=set()

        while n!=1:
            s=0
            if n in visited:
                return False
            visited.add(n)
            for i in str(n):
                s+=int(i)**2
            n=s

        return True

            