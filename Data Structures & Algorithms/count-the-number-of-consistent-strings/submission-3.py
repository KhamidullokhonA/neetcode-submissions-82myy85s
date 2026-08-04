class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        freq = Counter(allowed)
        count = 0
        for w in words:
            if all(c in allowed for c in w):
                count+=1
                

        return count

