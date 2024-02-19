"""
First recurring character

Given a string, return the first recurring letter that appears. If there are no
recurring letters, return None.

Example:
Imput: qqwertty
Output: q

Imput: qwerty
Output: None
"""

def first_recurring_char(s):

    seen_so_far = set()

    for c in s:
        if c in seen_so_far:
            return c 
        seen_so_far.add(c)

    return None

print(first_recurring_char('qwertty'))
#t