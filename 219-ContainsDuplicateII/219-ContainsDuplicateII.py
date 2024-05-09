class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        window = set()
        for right in range(len(nums)):
            if nums[right] in window:
                return True
            else:
            if right - left > k:
                window.remove(nums[left])
                left += 1
                window.add(nums[right])        
        return False
[
