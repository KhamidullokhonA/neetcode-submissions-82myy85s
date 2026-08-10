class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for k in freq.values():
            if k%2!=0:
                return False

        return True