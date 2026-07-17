class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        res = []
        n = len(nums)

        for num in nums:
            freq[num]+=1

        for k,v in freq.items():
            if v == 2:
                res.append(k)

        for i in range(1,n+1):
            if i not in freq:
                res.append(i)


        return res
        