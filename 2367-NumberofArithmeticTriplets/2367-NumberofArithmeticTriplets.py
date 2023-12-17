class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count = 0
        l = len(nums)
        for i in range(l-1, 1, -1):
            for j in range(i-1, 0, -1):
                if nums[i] - nums[j] == diff:
                    for k in range(j-1, -1, -1):
                        if nums[j] - nums[k] == diff:
                            count += 1
        return count
        
[
