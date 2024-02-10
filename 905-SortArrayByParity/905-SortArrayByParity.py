class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        ans = []
        for i in nums:
            if i % 2 == 0:
                ans.append(i)
            else:
                odd.append(i)
        ans.extend(odd)
        return ans
        
[
