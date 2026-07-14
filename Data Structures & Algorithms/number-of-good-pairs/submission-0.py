class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0

        for k in Counter(nums).values():
            res+=k*(k-1)/2

        return int(res)