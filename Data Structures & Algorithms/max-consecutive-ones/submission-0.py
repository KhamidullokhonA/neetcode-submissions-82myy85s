class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = count = 0
        for n in nums:
            
            
            if n == 1:
                count+=1
            else:
                count = 0


            maxC = max(maxC, count)

        return maxC
