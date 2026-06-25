class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for x in words:
            count = 0
            for y in words:
                if x in y:
                    count+=1

            if count>1:
                res.append(x)

        return res
