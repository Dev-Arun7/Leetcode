class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for i, num in enumerate(nums):
            if num == 1:
                distance = 0
                break
        for j in range(i+1, len(nums)):
            if nums[j] == 1:
                distance = 0
            else:
                distance += 1
                if distance < k:
                    return False

        return True
        
[
