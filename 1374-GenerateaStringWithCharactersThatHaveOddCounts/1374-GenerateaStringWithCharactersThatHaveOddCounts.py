    def generateTheString(self, n: int) -> str:
        result = ""
        if n % 2 == 0:

            result = "a" * (n - 1)
            result += 'b'
        else:
            result = 'a' * n
        return result
class Solution:
4
