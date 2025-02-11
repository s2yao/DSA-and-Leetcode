# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head

        temp = head
        curr = head.next
        temp.next = None

        while curr:
            nxt = curr.next
            curr.next = temp
            temp = curr
            curr = nxt
        
        return temp