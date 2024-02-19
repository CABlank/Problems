"""
Number of 1 bits

Given an integer, find the number of 1 bits it has.

Here's an example and some starting code.
"""

def one_bits(num):
    # Fill this in.
    count = 0
    while num > 0:
        if num & 1 == 1:
            count += 1
        num = num >> 1
    return count

print(one_bits(23))
# 4