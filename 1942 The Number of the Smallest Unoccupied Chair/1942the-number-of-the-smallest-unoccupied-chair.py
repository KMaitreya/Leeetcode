class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        # n=len(times)
        # occupied=[0]*n
        # occnum=0
        # t=0
        # j=0

        
        # for i in range(n):
        #     times[i].append(i)

        # times.sort()


        # while j<n:
        #     flg=1
        #     if t==times[j][0]:
        #         occupied[occnum]=times[j][1]
        #         j+=1
        #     if times[j][2]==targetFriend:
        #         return occnum
        #     for i in range(n):
        #         if occupied[i]>0:
        #             occupied[i]-=1
        #         if flg==1 and occupied[i]==0:
        #             occnum=i
        #             flg=0

        #     t+=1


        
        order = sorted(range(len(times)), key = lambda x: times[x][0])  # <-- 1)
        emptySeats, takenSeats = list(range(len(times))), []            # <-- 2)

        for i in order:                                                 # <-- 3)
            ar, lv = times[i]

            while takenSeats and takenSeats[0][0] <= ar:
                heappush(emptySeats, heappop(takenSeats)[1])
            seat = heappop(emptySeats)                                  # <-- 4)

            if i == targetFriend: return seat

            heappush(takenSeats,(lv, seat))
