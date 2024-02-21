class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count = 0
        for i in batteryPercentages:
            if i - count > 0:
                count += 1


        return count
        
[
