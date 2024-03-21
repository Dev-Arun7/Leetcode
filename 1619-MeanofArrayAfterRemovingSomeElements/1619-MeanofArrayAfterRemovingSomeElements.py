class Solution:
    def trimMean(self, arr: List[int]) -> float:
        sorted_arr = sorted(arr)
        
        # Sort the array in ascending order
        # Calculate the number of elements to remove (5% from each end)
        remove = int(len(arr) * 0.05)
        
        # Remove the smallest and largest elements
        trimmed_arr = sorted_arr[remove:len(arr)-remove]
        
        # Calculate the mean of the remaining elements
        mean = sum(trimmed_arr) / len(trimmed_arr)
        
        return mean

[
