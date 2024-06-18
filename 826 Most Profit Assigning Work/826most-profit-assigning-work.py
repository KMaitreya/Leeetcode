class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
    
        # Sort the workers by their ability
        worker.sort()
        
        # Variables to keep track of the total profit and maximum profit so far
        total_profit = 0
        max_profit = 0
        j = 0
        
        # Iterate over each worker
        for ability in worker:
            # Update the max_profit to the best available job for this worker's ability
            while j < len(jobs) and jobs[j][0] <= ability:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            # Add the best profit for this worker to the total profit
            total_profit += max_profit
        
        return total_profit