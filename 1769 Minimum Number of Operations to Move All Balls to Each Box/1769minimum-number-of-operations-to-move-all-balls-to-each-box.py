class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        storage=set()
        answer=[]

        for i, box in enumerate(boxes):
            if box=="1":
                storage.add(i)

        for i, box in enumerate(boxes):
            val=0
            for ones in storage:
                val+=abs(ones-i)
            answer.append(val)

        return answer