class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        freq = Counter(allowed)
        count = 0

        for w in words:
            each = Counter(w)
            if not (each.keys()-freq.keys()):
                count +=1

        return count