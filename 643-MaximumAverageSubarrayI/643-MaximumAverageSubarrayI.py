class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = len(nums)
        current_sum = sum(nums[:k])
        max_avg = current_sum / k
        for i in range(k, l):
            current_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, current_sum / k)
        return max_avg

[
