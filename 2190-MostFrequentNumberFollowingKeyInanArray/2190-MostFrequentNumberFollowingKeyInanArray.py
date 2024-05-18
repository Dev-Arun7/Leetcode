class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        hash = { }
        l = len(nums)
        for n in range(l - 1):
            if nums[n] == key:
                if nums[n + 1] in hash:
                    hash[nums[n + 1]] += 1
                else:
                    hash[nums[n + 1]] = 1
        for n in hash:
            if hash[n] > res[1]:
        res = [float('-inf'), float('-inf')]

        return res[0]
                res[0] = n
                res[1] = hash[n]
[
