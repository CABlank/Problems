# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Initialize previous node to None
        curr = head  # Start with the head as the current node

        while curr is not None:
            next_temp = curr.next  # Store the next node
            curr.next = prev  # Reverse the current node's pointer
            prev = curr  # Move the previous pointer one step forward
            curr = next_temp  # Move the current pointer one step forward

        return prev  # At the end, prev will be the new head of the reversed list



            
        