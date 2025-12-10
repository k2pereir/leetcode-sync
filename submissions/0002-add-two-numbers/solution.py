# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = l1 
        l1_int = ""
        while curr is not None: 
            l1_int = l1_int + str(curr.val)
            curr = curr.next
        curr = l2
        l2_int = ""
        while curr is not None: 
            l2_int = l2_int + str(curr.val)
            curr = curr.next
        l1_int = l1_int[::-1]
        l1_int = int(l1_int)
        l2_int = l2_int[::-1]
        l2_int = int(l2_int)
        add = l1_int + l2_int 
        add = str(add)
        add = add[::-1]
        answer = ListNode()
        add = str(add)
        curr = answer 
        for c in add: 
            curr.next = ListNode(int(c))
            curr = curr.next
        return answer.next

