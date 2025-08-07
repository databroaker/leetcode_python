# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return

        the_list = []

        for ref_list in [list1, list2]:
            ref = ref_list
            while True:
                if not ref:
                    break
                the_list.append(ref.val)
                ref = ref.next

        the_list.sort()

        ret_list = ListNode(the_list[0])
        ref = ret_list
        for val in the_list[1:]:
            ref.next = ListNode(val)
            ref = ref.next

        return ret_list


# [1,2,4]
# [1,3,4]

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

print(Solution().mergeTwoLists(list1, list2))