class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize:
            return False

        hashmap={}
  
        for card in hand:
            hashmap[card]=1+hashmap.get(card, 0)

        keys=list(hashmap.keys())
        heapq.heapify(keys)

        while keys:
            first=keys[0]
            for i in range(first, first+groupSize):
                if i not in hashmap:
                    return False
                hashmap[i]-=1
                if hashmap[i]==0:
                    if i!=keys[0]:
                        return False
                    heapq.heappop(keys)
        return True

            

            

        
        

