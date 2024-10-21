class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        one=0
        two=cost[-1]

        for i in range(len(cost)-2, -1, -1):
            one, two=two, min(one+cost[i], two+cost[i])

        return min(one, two)