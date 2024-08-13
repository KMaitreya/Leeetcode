class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(start, path, remaining_target):
            if remaining_target == 0:
                result.append(path)
                return
            if remaining_target < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Include candidates[i] in the combination
                backtrack(i + 1, path + [candidates[i]], remaining_target - candidates[i])

        candidates.sort()  # Sort to handle duplicates and help with pruning
        result = []
        backtrack(0, [], target)
        return result