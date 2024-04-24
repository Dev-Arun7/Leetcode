class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, ans, window_count = 0, 0, 0, 0
        zeros = 0
        l = len(nums)
        for right in range(l):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            window_count = right - left + 1
            ans = max(ans, window_count)

        return ans

[
