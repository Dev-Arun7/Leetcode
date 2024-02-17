class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maximum = 0
        frequency = 0
        my_set = set(nums)
        for i in my_set:
            frequency = nums.count(i)
            if frequency > maximum:
                maximum = frequency
            elif frequency == maximum:
        _sum = 0

                _sum = frequency
                _sum += frequency
        return _sum
        
[
