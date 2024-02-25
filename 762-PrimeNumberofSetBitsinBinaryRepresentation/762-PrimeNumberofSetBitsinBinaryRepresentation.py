class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1):
            temp = str(bin(i))[2:]
            bits = temp.count('1')
            if bits == 2:
                count += 1
            elif bits > 2:
                for j in range(2,bits):
                    if bits % j == 0:
                        break
                else:
                    count += 1
        return count
        
6
