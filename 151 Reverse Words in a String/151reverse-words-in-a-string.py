class Solution:
    def reverseWords(self, s: str) -> str:
        
        # for i in range(len(lst)):
        #     if lst[0]==' ':
        #         del lst[0]
        #         continue
        #     break

        # for i in range(len(lst)-1, -1, -1):
        #     if lst[i]==' ':
        #         del lst[i]
        #         continue
        #     break

        # # for i in range(1,len(lst)-1):
        # #     print(i, lst[i], lst)
        # #     if lst[i]==' ' and lst[i+1]==' ':
        # #         del lst[i+1]
        # #         i-=1
        # #         print(i)
        # #         print("deleted")

        # i=0
        # while i<len(lst)-1:
        #     if lst[i]==' ' and lst[i+1]==' ':
        #         del lst[i+1]
        #         i-=1


        # for char in lst:
        #     if char==" ":
        #         rev=st+char+rev
        #         st=""
        #         continue
        #     st+=char
        # rev=st+" "+rev
        # rev=rev[:-1]

        # NEW SOLUTION

        res=""
        temp=""
        flg=1

        for char in s:
            if char!=" ":
                temp+=char
                flg=0
            elif flg==0:
                res=temp+" "+res
                flg=1
                temp=""

        res=temp+" "+res

        del temp
        del flg

        return res.strip()