class Solution:
    def minimumPushes(self, word: str) -> int:
        
        hmap={}
        cnt=0
        s=0
        i=1


        for letter in word:
            if letter in hmap.keys():
                hmap[letter]+=1
            else:
                hmap[letter]=1

        hmap={k:v for k, v in sorted(hmap.items(), key=lambda item:item[1])}

        for key, value in reversed(hmap.items()):
            s+=i*value
            cnt+=1
            if cnt==8:
                cnt=0
                i+=1

        return s