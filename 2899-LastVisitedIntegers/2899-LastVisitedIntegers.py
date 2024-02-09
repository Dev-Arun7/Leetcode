        result = []
        nums = []
        count = 0
        for i in words:
            if i != 'prev':
                nums.append(i)
                count = 0
            else:
                count += 1
                pre = -(count)
                if len(nums) >= (count):
                    result.append(int(nums[pre]))
                else:
    def lastVisitedIntegers(self, words: list[str]) -> list[int]:
class Solution:
                    result.append(-1)
        return result


[
