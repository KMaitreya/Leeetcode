class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        # hmap={}
        # n=len(arr)
        # res=n*[1]
        
        # for i in range(n):
        #     if arr[i]in hmap.keys():
        #         hmap[arr[i]].append(i+1)
        #     else:
        #         hmap[arr[i]]=[i+1]

        # print(hmap)
        # for i in range(n):
        #     hmap[min(hmap.keys())]
            


        # arr.sort()
        # print(arr)

        # for i in range(len(arr)):
        #     arr[i][0]=i+1

        # arr.sort(key=lambda x:x[1])

        # return [x[0] for x in arr]

        if not arr:  # Handle empty array case
            return []
        
        # Step 1: Create a dictionary to store the element positions
        hmap = {}
        
        # Step 2: Sort the unique elements of the array
        sorted_unique = sorted(set(arr))  # Get sorted unique elements
        
        # Step 3: Assign ranks to elements
        for rank, value in enumerate(sorted_unique, start=1):
            hmap[value] = rank  # Map each element to its rank
        
        # Step 4: Replace elements in the original array with their rank
        res = [hmap[element] for element in arr]  # Transform the array based on rank
        
        return res