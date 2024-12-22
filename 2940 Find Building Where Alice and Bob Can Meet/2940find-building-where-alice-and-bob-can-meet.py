# class Solution:
#     def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
#         hmap={}
#         l=len(heights)
#         res=[]

#         # def helper(idx):
#         #     if idx not in hmap:
#         #         hmap[idx]=set()
#         #         hmap[idx].add(idx)
#         #         for k in range(idx+1, l):
#         #             if heights[k]>heights[idx]:
#         #                 hmap[idx].add(k)
#         #     return hmap[idx]

#         for i, j in queries:

#             flg=0
#             if heights[j]>heights[i]:
#                 res.append(j)
#                 continue

#             mval=heights[i]
#             mid=max(i, j)

#             print(mid, mval)
#             print("")

#             for k in range(mid, l):
#                 print(k, heights[k])
#                 if heights[k]>=mval:
#                     res.append(k)
#                     flg=1
#                     break
            
            
#             print("______")
#             print("______")

#             if flg==0:
#                 res.append(-1)
                
                    
#             # r=helper(i) & helper(j)
#             # if r:
#             #     res.append(min(r))
#             # else:
#             #     res.append(-1)

#         return res

class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        mono_stack = []
        result = [-1 for _ in range(len(queries))]
        new_queries = [[] for _ in range(len(heights))]
        for i in range(len(queries)):
            a = queries[i][0]
            b = queries[i][1]
            if a > b:
                a, b = b, a
            if heights[b] > heights[a] or a == b:
                result[i] = b
            else:
                new_queries[b].append((heights[a], i))

        for i in range(len(heights) - 1, -1, -1):
            mono_stack_size = len(mono_stack)
            for a, b in new_queries[i]:
                position = self.search(a, mono_stack)
                if position < mono_stack_size and position >= 0:
                    result[b] = mono_stack[position][1]
            while mono_stack and mono_stack[-1][0] <= heights[i]:
                mono_stack.pop()
            mono_stack.append((heights[i], i))
        return result

    def search(self, height, mono_stack):
        left = 0
        right = len(mono_stack) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mono_stack[mid][0] > height:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans