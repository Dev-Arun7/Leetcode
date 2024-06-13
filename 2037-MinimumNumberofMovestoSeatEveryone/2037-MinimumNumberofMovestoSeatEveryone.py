from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count = 0
        seats.sort()
        students.sort()

        for i in range(len(seats)):
            count += abs(seats[i] - students[i])

        return count
[
