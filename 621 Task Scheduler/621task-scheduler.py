class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hmap=Counter(tasks)
        queue=[]
        time=0
        maxheap=[-1*value for value in hmap.values()]
        heapq.heapify(maxheap)

        while maxheap or queue:
            time+=1
            if maxheap:
                task=heapq.heappop(maxheap)
                if task!=-1:
                    queue.append([task+1,time+n])
            if queue and queue[0][1]==time:
                heapq.heappush(maxheap, queue.pop(0)[0])

        return time

        