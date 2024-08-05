class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:

        hmap={}
        
        for player in pick:
            if player[0] in hmap.keys():
                hmap[player[0]].append(player[1])
            else:
                hmap[player[0]]=[player[1]]

        cnt=0

        print(hmap)

        for key, value in hmap.items():
            if key==0:
                cnt+=1
            else:
                countMap={}
                for num in value:
                    if num in countMap.keys():
                        countMap[num]+=1
                    else:
                        countMap[num]=1
                    if countMap[num]==key+1:
                        cnt+=1
                        break


        return cnt