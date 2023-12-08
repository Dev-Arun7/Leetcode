class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i, emp in enumerate(hours):
            if emp >= target:
                count += 1
        return count
            