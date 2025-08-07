# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return ListNode()
        last_val = head.val
        new_list = ListNode(last_val)
        nl_ref = new_list
        ref = head.next
        while True:
            curr_val = ref.val
            if curr_val != last_val:
                nl_ref.next = ListNode(ref.val)
                nl_ref = nl_ref.next
            last_val = ref.val
            ref = ref.next
            if not ref:
                break

        return new_list

print(Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))))