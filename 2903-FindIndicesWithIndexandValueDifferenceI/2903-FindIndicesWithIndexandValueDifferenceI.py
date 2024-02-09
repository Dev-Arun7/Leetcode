class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        l = len(nums)
        result = []
        for i in range(l - indexDifference):
            for j in range(i + indexDifference, l):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    result.append(i)
                    result.append(j)
                    return result

        return [-1, -1]
        
[
