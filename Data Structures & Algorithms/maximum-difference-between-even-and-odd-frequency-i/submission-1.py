class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for c in s:
            if c in freq:
                freq[c]+=1
            else:
                freq[c]=1

        lst = list(freq.values())

        even = [e for e in lst if e%2==0]
        odd = [o for o in lst if o%2==1]

        return max(odd)-min(even)