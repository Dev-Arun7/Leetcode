class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result = []
        l = len(nums)
        for i in range(0,l,2):
            for j in range(nums[i]):
                result.append(nums[i+1])
        return result


[
