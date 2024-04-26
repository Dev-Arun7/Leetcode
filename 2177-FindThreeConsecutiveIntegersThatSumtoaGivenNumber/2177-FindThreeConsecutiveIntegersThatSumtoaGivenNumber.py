class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        if num / 3 == num // 3:
            ans.append(num // 3)
            ans.append((num // 3) + 1)
        return ans
            ans.append((num // 3) - 1)
        
3
