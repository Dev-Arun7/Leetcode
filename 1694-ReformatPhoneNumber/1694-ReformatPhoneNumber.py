        while len(nums) > 4:  # While there are more than 4 digits left
            ans += ''.join(nums[:3]) + '-'  # Add the first three digits and a hyphen
            nums = nums[3:]  # Remove the first three digits from the list

        if len(nums) <= 3:  # If there are 3 or fewer digits left
            ans += ''.join(nums)  # Add them directly
            ans += ''.join(nums[:2]) + '-'  # Add the first two digits and a hyphen
            ans += ''.join(nums[2:])  # Add the remaining two digits
        else:  # If there are exactly 4 digits left

        return ans
        nums = [i for i in number if i.isdigit()]  # Fix the list comprehension syntax

        ans = ''
    def reformatNumber(self, number: str) -> str:
class Solution:
"
