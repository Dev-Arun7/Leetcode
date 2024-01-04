class Solution:
    def splitNum(self, num: int) -> int:

        str_num = ''.join(sorted(str(num)))
        return int(str_num[::2]) + int(str_num[1::2])
        
4
