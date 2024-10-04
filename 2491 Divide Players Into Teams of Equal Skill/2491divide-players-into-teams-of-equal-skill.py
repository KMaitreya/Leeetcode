class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        l=1
        r=len(skill)-2
        
        skill.sort()

        total=skill[0]*skill[-1]
        s=skill[0]+skill[-1]

        while l<r:
            if s==skill[l]+skill[r]:
                total+=skill[l]*skill[r]
                l+=1
                r-=1
            else:
                return -1

        return total