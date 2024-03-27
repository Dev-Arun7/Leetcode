class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        product = 1
        for r in range(len(nums)):
            product *= nums[r]
            if product >= k:
                while product >= k and left <= r:
                    product /= nums[left]
                    left += 1
        if k <= 1:
            return 0
            count += r - left + 1
        return count

        
[
