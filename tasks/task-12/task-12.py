# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        half = 0
        i = 0

        while curr is not None:
            count += 1
            curr = curr.next

        curr = head

        if count % 2 == 0:   
            half = count// 2
            while curr is not None and i < half:
                i += 1
                curr = curr.next
            return curr

        else:
            half = floor(count / 2)
            while curr is not None and i < half:
                i += 1
                curr = curr.next
            return curr