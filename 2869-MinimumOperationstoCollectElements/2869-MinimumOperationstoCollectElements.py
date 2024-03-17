class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = []
        l = len(nums)
        for i in range(l-1, -1, -1):
            temp = nums.pop()
            if temp <= k and temp not in result:
                result.append(temp)
                if len(result) == k:
                    return l-i
        
[
