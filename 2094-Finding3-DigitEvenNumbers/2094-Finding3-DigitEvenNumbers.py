        result = []
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
class Solution:
        for i in range(100, 1000, 2):
            temp = str(i)
            for j in temp:
                    if temp.count(j) > digits.count(int(j)):
                        break
                if int(j) in digits:
            else:
                result.append(i)
                else:
                    break
[
