# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count = 0
        curr = head
        elements = []
        while curr:
            count += 1
            elements.append(curr.val)
            curr = curr.next
        # so that gives me the length of the linked list
        remove = count - n
        dummy = ListNode(0)
        tail = dummy
        for i, val in enumerate(elements, start = 0):
            if i != remove:
                tail.next = ListNode(val)
                tail = tail.next
        return dummy.next
