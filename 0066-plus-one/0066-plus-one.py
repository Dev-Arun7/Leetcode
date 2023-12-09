class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        str_digit = ""
        result = []
        while len(digits) > 0:
            str_digit += str(digits.pop(0))
        int_digit = int(str_digit)
        int_digit += 1
        str_digit = str(int_digit)
        for i in str_digit:
            result.append(int(i))
        return result
