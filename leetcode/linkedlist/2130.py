# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        ret = 0
        fast = head
        slow = head
        temp = None

        while fast and fast.next:
            fast = fast.next.next
            NextNode = slow.next
            slow.next = temp
            temp = slow
            slow = NextNode

        while slow:
            ret = max(ret, slow.val + temp.val)
            slow = slow.next
            temp = temp.next

        return ret