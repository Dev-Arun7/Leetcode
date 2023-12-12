class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        sum = 0
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                sum += i
        return 0 if count == 0 else int(sum / count)
                
                count += 1
        
[
