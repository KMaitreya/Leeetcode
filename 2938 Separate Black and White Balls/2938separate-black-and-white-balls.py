class Solution:
    def minimumSteps(self, s: str) -> int:
        
        # count=Counter(s)

        # n=max(count)
        # mcnt=0
        # cnt=0
        # res=s[:count[n]]

        # for i in range(len(s)-count[n]+1):
        #     temp=s[i:i+count[n]]
        #     tempcnt=Counter(temp)
        #     cnt=tempcnt[n]
        #     if cnt>mcnt:
        #         mcnt=cnt
        #         res=temp

        # print(temp)


        # return 0

        cnt=0
        z=0
        res=0

        for x in s[::-1]:
            if x=="0":
                res+=cnt*z
                z+=1
                cnt=0
            else:
                cnt+=1

        res+=cnt*z

        return res

