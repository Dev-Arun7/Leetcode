class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            temp = str(i)
            for j in temp:
                result.append(int(j))
        return result
        
[
