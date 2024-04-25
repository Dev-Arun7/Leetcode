    def maxScore(self, cardPoints: List[int], k: int) -> int:
class Solution:
        total_points = sum(cardPoints)
        window_size = len(cardPoints) - k
        min_window_sum = float('inf')
        current_window_sum = 0

        # Calculate the sum of the first window
        for i in range(window_size):
            current_window_sum += cardPoints[i]
        
        min_window_sum = min(min_window_sum, current_window_sum)

        # Slide the window and update the minimum window sum
        for i in range(window_size, len(cardPoints)):
            current_window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, current_window_sum)

        return total_points - min_window_sum

[
