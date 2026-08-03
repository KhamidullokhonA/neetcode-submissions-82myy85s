class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()

        for k in nums1:
            if k in nums2:
                res.add(k)

        return list(res)

        