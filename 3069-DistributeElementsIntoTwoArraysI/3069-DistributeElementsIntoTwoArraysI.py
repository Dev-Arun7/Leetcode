    def resultArray(self, nums: List[int]) -> List[int]:
class Solution:
        arr1 = [nums.pop(0)]
        arr2 = [nums.pop(0)]
        for i, n in enumerate(nums):
            if arr1[-1] > arr2[-1]:
                arr1.append(n)
            else:
                arr2.append(n)
        result = arr1 + arr2
        return result
        
[
