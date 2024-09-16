class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        times=[]
        diff, mdiff=0, 3000

        for point in timePoints:
            times.append(int(point[:2])*60+int(point[3:]))

        times.sort()
        times.append(times[0]+1440)

        for i in range(1, len(times)):
            diff=times[i]-times[i-1]
            mdiff=min(mdiff, diff)

        return min(mdiff, diff)