class Solution:
    def compress(self, chars: List[str]) -> int:
        
        cnt=0
        i=0
        temp=[]
        chars.append(" ")

        while chars[i] != " ":
            if i < len(chars) - 1 and chars[i] == chars[i + 1]:
                cnt += 1
            else:
                temp.append(chars[i])
                if cnt>0:
                    cnt_digits = [d for d in str(cnt + 1)]
                    temp.extend(cnt_digits)
                cnt = 0
            i += 1

        chars[:] = temp


        return len(chars)
