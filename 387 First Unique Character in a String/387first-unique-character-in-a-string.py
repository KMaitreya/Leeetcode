class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict={}
        for i in range(len(s)):
            dict[s[i]]=s.count(s[i])
            if dict[s[i]]==1:
                return i

        return -1

        