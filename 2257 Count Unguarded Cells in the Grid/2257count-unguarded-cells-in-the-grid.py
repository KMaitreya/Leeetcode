class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        visited=set()
        guards=set(map(tuple, guards))
        walls=set(map(tuple, walls))

        visited|=guards
        visited|=walls
        
        for guard in guards:

            #down
            for i in range(guard[0]+1, m):
                if (i, guard[1]) in walls or (i, guard[1]) in guards:
                    break
                visited.add((i, guard[1]))

            #up
            for i in range(guard[0]-1, -1, -1):
                if (i, guard[1]) in walls or (i, guard[1]) in guards:
                    break
                visited.add((i, guard[1]))

            #left
            for j in range(guard[1]-1, -1, -1):
                if (guard[0], j) in walls or (guard[0], j) in guards:
                    break
                visited.add((guard[0], j))

            #right
            for j in range(guard[1]+1, n):
                if (guard[0], j) in walls or (guard[0], j) in guards:
                    break
                visited.add((guard[0], j))

        return (m*n)-len(visited)#