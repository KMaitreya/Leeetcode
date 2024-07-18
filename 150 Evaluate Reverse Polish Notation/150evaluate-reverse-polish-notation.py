class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        flg=0
        i=0

        while len(tokens)>1:
            if tokens[i]=="/":
                tokens[i]=int(tokens[i-2])/int(tokens[i-1])
                flg=1
            elif tokens[i]=="*":
                tokens[i]=int(tokens[i-2])*int(tokens[i-1])
                flg=1
            elif tokens[i]=="-":
                tokens[i]=int(tokens[i-2])-int(tokens[i-1])
                flg=1
            elif tokens[i]=="+":
                tokens[i]=int(tokens[i-2])+int(tokens[i-1])
                flg=1

            if flg==1:
                del tokens[i-1]
                del tokens[i-2]
                i=0
            
            flg=0
            i+=1

        return int(tokens[0])

