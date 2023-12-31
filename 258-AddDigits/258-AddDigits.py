class Solution:
    def addDigits(self, num: int) -> int:
        _sum = num
        while _sum > 9:
            temp = _sum
            _sum = 0
            while temp > 0:
                temp //= 10
        return _sum
                _sum += temp % 10
        
3
