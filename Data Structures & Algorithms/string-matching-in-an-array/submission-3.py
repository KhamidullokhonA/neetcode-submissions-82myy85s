class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for x in words:
            for y in words:
                if x != y and x in y:
                    res.append(x)
                    break

        return res
