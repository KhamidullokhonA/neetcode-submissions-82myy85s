class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = [c for c in s]

        
        l, r = 0, 0
        while r<len(s):
            if  s[r] == '1':
                s[l], s[r] = s[r], s[l]
                l+=1
            r+=1

        s[l-1], s[len(s)-1] = s[len(s)-1], s[l-1]

        return "".join(s)

            