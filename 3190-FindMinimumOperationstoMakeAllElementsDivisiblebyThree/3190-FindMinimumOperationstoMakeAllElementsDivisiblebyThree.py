class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for n in nums:
            if n % 3 != 0:
                operations += 1

        return operations
        
[
[1,2,3,4]
[3,6,9]
3
0
3
0
