class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path)==k:
                res.append(path.copy())
                return 

            

            for i in range(start, n):
                if i+1 in path:
                    continue 
                path.append(i+1)
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res