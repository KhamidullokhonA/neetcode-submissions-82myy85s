class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, 0 

        while r<len(nums):
            if nums[r]% 2:
                r+=1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                r+=1
                l+=1

        return nums