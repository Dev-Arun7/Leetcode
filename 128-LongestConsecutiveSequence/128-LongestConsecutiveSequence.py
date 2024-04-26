class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in num_set:
                while (n + length) in num_set:
            length = 0
            # Initialize length as zero
                    length +=1
                
                longest = max(longest, length)
        return longest
        
[
