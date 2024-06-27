class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        # hmap={}
        # n=len(edges)

        # for nodes in edges:
        #     for node in nodes:
        #         hmap[node]=hmap.get(node, 0)+1

        # for key, value in hmap.items():
        #     if value==n:
        #         return key

        ## Better method

        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]