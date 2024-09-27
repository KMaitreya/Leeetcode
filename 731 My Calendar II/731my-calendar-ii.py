class MyCalendarTwo:

    def __init__(self):
        self.bookings=[]
        self.overlaps=[]

    def book(self, start: int, end: int) -> bool:
        
        # First, check if the new event would cause a triple booking by overlapping with any double booking
        for os, oe in self.overlaps:
            if max(start, os) < min(end, oe):
                return False  # This would cause a triple booking
        
        # Check the new event against all single bookings, and add overlapping parts to overlaps
        for bs, be in self.bookings:
            overlap_start = max(start, bs)
            overlap_end = min(end, be)
            if overlap_start < overlap_end:
                # There's an overlap, add this to the double bookings list
                self.overlaps.append((overlap_start, overlap_end))
        
        # If we get here, it means no triple booking would happen, so we can book the event
        self.bookings.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)