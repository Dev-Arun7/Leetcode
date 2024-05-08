# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        prev = head
        while curr:
            gcd = math.gcd(curr.val, prev.val)
            gcd_node = ListNode(gcd)
            prev.next = gcd_node
            gcd_node.next = curr
            curr = curr.next
            prev = curr

        return head

[
