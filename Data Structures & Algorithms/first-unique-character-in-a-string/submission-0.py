class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        
        for i, k in enumerate(s):
            if freq[k]==1:
                return i

        return -1