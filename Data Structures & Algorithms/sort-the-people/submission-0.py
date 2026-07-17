class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        freq = defaultdict(int)
        for name, height in zip(names, heights):
            freq[height] = name

        res = [freq[k] for k in sorted(freq)]
        return res[::-1]