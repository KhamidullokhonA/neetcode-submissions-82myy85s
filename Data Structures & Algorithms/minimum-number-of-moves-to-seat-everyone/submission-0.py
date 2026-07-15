class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0

        for seats, students in zip(seats, students):
            res+=abs(students-seats)

        return res

        