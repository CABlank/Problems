"""
Find subtree

Given 2 binary trees t and s, find if s has an equal subtree in t,
where the structure and the values are the same. Return True if it
exists, otherwise return False.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"

def same_tree(s, t):
    if not s and not t:
        return True
    if s and t and s.value == t.value:
        return same_tree(s.left, t.left) and same_tree(s.right, t.right)
    return False

def find_subtree(s, t):
    if not t:
        return False
    if same_tree(s, t):
        return True
    return find_subtree(s, t.left) or find_subtree(s, t.right)

# Test the code
t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(2))

print(find_subtree(s, t))  # Should return True
