        for i, digit in enumerate(binary):
            if i % 2 == 0:
                if digit == "1":
                    even += 1
            else:
                if digit == "1":
                    odd += 1
        return [even, odd]
        binary = bin(n)[2:][::-1]
        even = 0
        odd = 0
class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        
      

1
