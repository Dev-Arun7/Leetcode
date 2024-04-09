        num2 = ""
        n1 = l1
        n2 = l2
        while n1:
            num1 += str(n1.val)
            n1 = n1.next
        num1 = num1[::-1]

        while n2:
            num2 += str(n2.val)
            n2 = n2.next
        num2 = num2[::-1]

        result = str(int(num1) + int(num2))

        dummy_head = ListNode()
        current = dummy_head

        for digit in result:
            current.next = ListNode(val=int(digit))
            current = current.next
        result = result[::-1]

        return dummy_head.next

        
[
