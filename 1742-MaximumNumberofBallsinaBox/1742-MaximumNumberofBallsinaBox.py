class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        count = 0
        for digit in range(lowLimit, highLimit + 1):
            str_digit = str(digit)
            digit_sum = sum(int(num) for num in str_digit)
            if digit_sum not in boxes:
                boxes[digit_sum] = 1
            else:
                boxes[digit_sum] += 1
        
        for box in boxes:
            count = max(count, boxes[box])

        return count
        
1
