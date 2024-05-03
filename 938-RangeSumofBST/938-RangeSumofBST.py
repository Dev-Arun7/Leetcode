class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        # Initialize sum
        total_sum = 0
        
        # If the current node's value is within the range, add it to the sum
        if low <= root.val <= high:
            total_sum += root.val
        
        # Recursively search left and right subtrees
        total_sum += self.rangeSumBST(root.left, low, high)
        total_sum += self.rangeSumBST(root.right, low, high)
        
        return total_sum
#         self.right = right
#         self.left = left
#         self.val = val
#     def __init__(self, val=0, left=None, right=None):
# class TreeNode:
[
