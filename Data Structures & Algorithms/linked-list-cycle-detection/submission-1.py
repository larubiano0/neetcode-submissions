# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while slow_pointer and fast_pointer:
            fast_pointer = fast_pointer.next
            if (fast_pointer) and (slow_pointer.val == fast_pointer.val):
                return True
            if slow_pointer:
                slow_pointer = slow_pointer.next
            if fast_pointer:
                fast_pointer = fast_pointer.next
        return False