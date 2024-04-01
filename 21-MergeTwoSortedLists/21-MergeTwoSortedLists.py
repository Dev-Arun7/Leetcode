                list1 = list1.next 
                tail.next = list2
                list2 = list2.next 
            tail = tail.next
        
        # Append remaining nodes from list1 or list2
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next

            else:
                tail.next = list1
            if list1.val < list2.val:
        tail = dummy

        while list1 and list2:
        dummy = ListNode()
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
class Solution:
[
