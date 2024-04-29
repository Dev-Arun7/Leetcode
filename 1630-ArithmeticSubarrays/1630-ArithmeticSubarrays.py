class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        length = len(l)
        for i in range(length):
            temp = nums[l[i] : r[i] + 1]
            for j in range(len(temp) - 1):
            diff = temp[1] - temp[0]
                if temp[j + 1] - temp[j] != diff:
        ans = []
                    ans.append(False)
            else:
                ans.append(True)
                    break
        
            temp.sort()
        return ans

[
