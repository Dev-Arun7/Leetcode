        while len(digits) > 1:
            status = True
            i = 0
            while i < len(digits):
                if status == True:
                    temp.append(min(digits[i], digits[i+1]))
                    i += 2
                    status = False
                else:
                    temp.append(max(digits[i], digits[i+1]))
                    i += 2
                    status = True
            digits.clear()

            digits = temp[::]
        digits = nums[::]
        temp = []
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:

            temp.clear()
        return digits[0]
        
[
