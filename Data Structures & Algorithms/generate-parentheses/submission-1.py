class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(string))
                return 

            if openN < n:
                string.append("(")
                backtrack(openN+1, closedN)
                string.pop()

            if closedN<openN:
                string.append(")")
                backtrack(openN, closedN+1)
                string.pop()

            
        backtrack(0,0)
        return res


    