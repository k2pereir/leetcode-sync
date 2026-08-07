# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def middle(head):
            if not head:
                return head
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge(one, two):
            temp = ListNode()
            tail = temp
            while one and two:
                if one.val < two.val:
                    tail.next = one
                    one = one.next
                else:
                    tail.next = two
                    two = two.next
                tail = tail.next
            if one:
                tail.next = one
            if two:
                tail.next = two
            return temp.next
            
        mid = middle(head)
        after = mid.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(after)
        return merge(left, right)
