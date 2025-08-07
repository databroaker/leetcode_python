
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        answer_list = ListNode()
        tracker = answer_list
        carry = 0
        while True:
            val1 = l1.val
            val2 = l2.val
            answer = val1 + val2 + carry
            carry = 0
            test = answer // 10
            if test:
                answer = answer - 10
                carry = 1

            tracker.val = answer


            if not l1.next and not l2.next:
                if carry:
                    tracker.next = ListNode(carry)
                break

            tracker.next = ListNode()
            tracker = tracker.next

            if l1.next:
                l1 = l1.next
            else:
                l1 = ListNode()
            if l2.next:
                l2 = l2.next
            else:
                l2 = ListNode()

        print(answer_list)

        return answer_list


# Best Solution
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = carry + x + y
            carry = sum // 10
            current.next = ListNode(sum%10)
            current = current.next

            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next

print(Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))