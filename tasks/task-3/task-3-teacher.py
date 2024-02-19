"""
H-Index

The h-index is a metric that attempts to measure the productivity and citation impact of the
publication of a scholar. The definition of the h-index is if a scholar has at least h of their
papers cited h times.

Given a list of publications of the number of citations a scholar has, find their h-index.

Example:
Input: [3, 5, 0, 1, 3]
Output: 3
Explanation:
There are 3 publications with 3 or more citations, hence the h-index is 3.

Here's a starting point:
"""

def hIndex(publications):
    n = len(publications)
    citations = [0] * (n + 1)

    for i in publications:
        if i < n:
            citations [i] += 1
        else:
            citations [n] += 1

    total = 0
    i = n
    while i >= 0:
        total += citations [i]
        if total >= i:
            return i
        i -= 1
    return i
    # Fill this in.

print (hIndex([100, 5, 6, 7, 5]))
# 3
