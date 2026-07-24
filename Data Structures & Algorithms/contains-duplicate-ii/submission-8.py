class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        l, r = 0, 0

        while r<len(nums):
            if r-l<=k:
                if nums[r] in seen:
                    return True
                seen.add(nums[r])
                r+=1

            else:
                seen.remove(nums[l])
                l+=1
                

            
            

        return False



            




            



            