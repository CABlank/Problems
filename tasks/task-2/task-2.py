class Node:
    def __init__(self, value, next=None):
        self.value  = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value}, {self.next})"
    
def swap_every_two(llist):
    head = llist
    curr = head
    while curr is not None and curr.next is not None:
        curr.value, curr.next.value = curr.next.value, curr.value
        curr = curr.next.next
    
    return head


llist = Node(2, Node(1, Node(4, Node(3, Node(6, Node(5, Node(7)))))))  
print(swap_every_two(llist))