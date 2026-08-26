# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, node):
        curr = node
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head
        count = 1

        while curr and count < k:
            curr = curr.next
            count += 1

        if curr is None:
            return head

        next_group = curr.next
        curr.next = None

        result = self.reverse(head)

        head.next = self.reverseKGroup(next_group, k)

        return result