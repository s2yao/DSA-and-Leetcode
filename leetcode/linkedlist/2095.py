# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast = head
        slow = head
        temp = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next

        if fast == slow:
            return None

        temp.next = slow.next
        slow.next = None

        return head
        
        



head = [1,3,4,7,1,2,6]
print(Solution.deleteMiddle(head))
