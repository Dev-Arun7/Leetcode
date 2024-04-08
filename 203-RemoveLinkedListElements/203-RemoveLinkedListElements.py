# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev, cur = dummy, head
        while cur:
            next = cur.next
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = next
        return dummy.next

[
