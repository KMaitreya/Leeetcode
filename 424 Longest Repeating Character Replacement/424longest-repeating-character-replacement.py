class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # m=0
        # mcnt=0
        # hmap={}
        # l=0

        # for r in range(len(s)):
        #     hmap[s[r]]=1+hmap.get(s[r], 0)
        #     m=max(m, hmap[s[r]])
        #     while r-l+1-m>k:
        #         hmap[s[l]]-=1
        #         l+=1
        #     mcnt=max(mcnt, r-l+1)

        # return mcnt

        m=0
        mcnt=0
        hmap={}
        l=0
        res=""

        for r in range(len(s)):
            hmap[s[r]]=1+hmap.get(s[r], 0)
            m=max(m, hmap[s[r]])
            if r-l+1-m>k:
                hmap[s[l]]-=1
                l+=1
            # mcnt=max(mcnt, r-l+1)
            if r-l+1>mcnt:
                res=s[l:r+1]
                mcnt=r-l+1


        return mcnt

        






              

            