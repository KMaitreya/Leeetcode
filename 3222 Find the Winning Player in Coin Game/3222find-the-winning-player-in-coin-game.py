class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        
        cntx, cnty=0, 0

        if x<1 or y<4:
            return "Bob"

        def increment(cntx, cnty):
            return cntx+1, cnty+4

        while True:
            cntx, cnty=increment(cntx, cnty)

            if x==cntx or y-cnty<4:
                return "Alice"

            cntx, cnty=increment(cntx, cnty)

            if x==cntx or y-cnty<4:
                return "Bob"