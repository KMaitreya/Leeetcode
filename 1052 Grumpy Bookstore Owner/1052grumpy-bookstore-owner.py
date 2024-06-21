class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
    
        # Step 1: Calculate the base satisfaction
        base_satisfaction = 0
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfaction += customers[i]

        # Step 2: Find the maximum additional satisfaction using the sliding window technique
        additional_satisfaction = 0
        current_window_satisfaction = 0
        
        # Initial window (first 'minutes' duration)
        for i in range(minutes):
            if grumpy[i] == 1:
                current_window_satisfaction += customers[i]
        
        # Set the initial maximum to the current window satisfaction
        additional_satisfaction = current_window_satisfaction
        
        # Slide the window across the rest of the array
        for i in range(minutes, n):
            if grumpy[i] == 1:
                current_window_satisfaction += customers[i]
            if grumpy[i - minutes] == 1:
                current_window_satisfaction -= customers[i - minutes]
            
            additional_satisfaction = max(additional_satisfaction, current_window_satisfaction)
        
        # Step 3: Return the total maximum satisfied customers
        return base_satisfaction + additional_satisfaction