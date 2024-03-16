class Solution:
    def distinctIntegers(self, n: int) -> int:
        nums = [n]
        count = 0
        while count < len(nums):
            count += 1
            num = nums[count - 1]
            for i in range(1,num):
                if num % i == 1:
                        nums.append(i)
        return len(nums)
                    if i not in nums:
        
5
