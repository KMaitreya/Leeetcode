class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            t=target-numbers[i]
            if t in numbers:
                if numbers[i]==t:
                    return [i+1, i+2]
                return [i+1, numbers.index(t)+1]