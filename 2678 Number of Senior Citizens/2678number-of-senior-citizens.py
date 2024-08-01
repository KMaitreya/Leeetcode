class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        cnt=0

        for data in details:
            if int(data[11]+data[12])>60:
                cnt+=1

        return cnt