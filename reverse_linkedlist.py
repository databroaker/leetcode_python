# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head:
            return head

        l = []
        curr = head
        while True:
            if curr:
                l.insert(0, curr.val)
                curr = curr.next
            else:
                break

        new_list = ListNode()
        ref = new_list
        while True:
            val = l.pop(0)
            ref.val = val
            ref.next = ListNode()
            ref = ref.next
            if len(l) == 0:
                break

        return new_list

# [1,2,3,4,5]
head = ListNode(1, ListNode(2))
print(Solution().reverseList(head))