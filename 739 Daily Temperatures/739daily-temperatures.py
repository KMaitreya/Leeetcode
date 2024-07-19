class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # n=len(temperatures)
        # op=[]

        # for i in range(n):
        #     cnt=0
        #     flg=0
        #     for j in range(i+1, n):
        #         cnt+=1
        #         if temperatures[j]>temperatures[i]:
        #             op.append(cnt)
        #             flg=1
        #             break
        #     if flg==0:
        #       op.append(0)

        # return op

        n = len(temperatures)
        result = [0] * n  # Initialize the result list with 0s
        stack = []  # Stack to keep indices of temperatures

        for i in range(n):
            # While there are indices in the stack and the current temperature is greater than the temperature at the index of the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index  # Calculate the number of days to wait
            stack.append(i)  # Add the current index to the stack

        return result
