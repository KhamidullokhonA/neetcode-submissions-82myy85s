class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -1*gifts[i]

        heapq.heapify(gifts)

        for _ in range(k):
            num = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(num)))

        return -sum(gifts)