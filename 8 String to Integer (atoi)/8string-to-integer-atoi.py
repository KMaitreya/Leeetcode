class Solution:
    def myAtoi(self, s: str) -> int:


        ### FIRST ATTEMPT
        
        # flg=0
        # flg2=0
        # flg3=0
        # op=""
        
        # for char in s:
        #     if char==" ":
        #         pass
        #     elif not char.isdigit():
        #         if char=="-" and flg2==0:
        #             flg=1
        #         elif flg3==0:
        #             return 0
        #         else:
        #             break
        #     elif char.isdigit():
        #         flg2=1
        #         flg3=1
        #         op+=char
        #     else:
        #         break
        
        # print(op)

        # if op=="":
        #     return 0

        
        # if flg==1:
        #     op=-1*int(op)
        # else:
        #     op=int(op)

        # if op<pow(-2, 31):
        #     return pow(-2,31)
        # elif op>pow(2,31)-1:
        #     return pow(2,31)-1
        # else:
        #     return op


        #### SECOND ATTEMPT

        # op=""
        # flg=0
        # flg1=0

        # if "+-" in s or "-+" in s or "+ " in s or "- " in s:
        #     return 0

        # for i in range(len(s)):
        #     if s[i]=="-" and flg==0:
        #         flg1=1
        #     elif s[i].isdigit():
        #         flg=1
        #         op+=s[i]
        #     elif s[i] not in " +-" or flg==1:
        #         break


        # if op=="":
        #     op=0
        # else:
        #     if flg1==1:
        #         op=-int(op)
        #     else:
        #         op=int(op)

        # if op<pow(-2, 31):
        #     return pow(-2,31)
        # elif op>pow(2,31)-1:
        #     return pow(2,31)-1
        # else:
        #     return op


        ###### THIRD ATTEMPT

        op=""
        flg=0
        flg1=0
        cnt=0


        for char in s:
            if char==" " and flg1==0:
                cnt+=1
            elif not char.isdigit():
                flg1=1
                op+=char
            else:
                break

        n=len(op)

        if n==0:
            pass
        elif n==1:
            if op[0]=="-":
                flg=1
            elif op[0]=="+":
                pass
            else:
                return 0
        else:
            return 0

        op=""

        s=s[n+cnt:]

        for char in s:
            if char.isdigit():
                op+=char
            else:
                break


        if op=="":
            op=0
        else:
            if flg==1:
                op=-int(op)
            else:
                op=int(op)

        if op<pow(-2, 31):
            return pow(-2,31)
        elif op>pow(2,31)-1:
            return pow(2,31)-1
        else:
            return op

        