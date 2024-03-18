# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        # Initialize pointers for odd and even nodes
        odd = head
        even = head.next
        evenHead = even  # To remember the start of even nodes

        # Traverse the list, rearranging odd and even nodes
        while even and even.next:
            odd.next = even.next  # Link the next odd node
            odd = odd.next  # Move the odd pointer
            even.next = odd.next  # Link the next even node
            even = even.next  # Move the even pointer

        # Connect the end of odd nodes to the beginning of even nodes
        odd.next = evenHead

        return head
