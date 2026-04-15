class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if not digits:
            return []

        def backtrack(start, path):
            if start==len(digits):
                res.append("".join(path))
                return 

            for char in mapping[digits[start]]:
                path.append(char)
                backtrack(start+1, path)
                path.pop()

        backtrack(0,[])
        return res

            