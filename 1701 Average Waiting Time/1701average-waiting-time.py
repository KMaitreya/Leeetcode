class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        curr=0
        total=0
        
        for arrival, time in customers:
            if curr<arrival:
                curr=arrival
            curr+=time
            total+=curr-arrival

        return total/len(customers)