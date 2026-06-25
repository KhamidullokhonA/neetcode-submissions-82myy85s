class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst = [1]

        for i in range(1, rowIndex+1):
            new = lst[-1]*(rowIndex-i+1)/i
            lst.append(int(new))

        return lst