        result = []
        temp = []
        _count = 0
        temp_list = nums[::]
        nums_set = set(nums)
        while temp_list:
            _count += 1
            temp = []
            for i in nums_set:
                if nums.count(i) >= _count:
                    temp.append(i)
                    temp_list.remove(i)
            result.append(temp)
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
class Solution:
[
