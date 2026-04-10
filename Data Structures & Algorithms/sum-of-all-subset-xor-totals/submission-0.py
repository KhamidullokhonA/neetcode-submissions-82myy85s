class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        total = 0 

        def backtrack(start, path):
            res.append(path.copy())
            nonlocal total
            xorr = 0
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

            for each in path:
                xorr^= each
            total+= xorr
            

            

        backtrack(0, [])

        return total