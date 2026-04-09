class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            if total==target:

                res.append(path.copy())
                return 

            for i in range(start, len(nums)):
                if total>target:
                    return 
                path.append(nums[i])
                backtrack(i, path, total + nums[i])  # stay at i because reuse allowed
                path.pop()

            
        backtrack(0, [], 0)
        return res


            

            