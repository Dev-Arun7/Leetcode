class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        same = []
        right = []
        for n in nums:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                same.append(n)
        return left + same + right
        
[
