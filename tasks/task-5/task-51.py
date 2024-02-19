"""
Running Median

You are given a stream of numbers. Compute the median for each new element .

Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]

Here's a starting point:

"""
import heapq

def get_median(max_heap, min_heap):
    if len(min_heap) > len(max_heap):
        return min_heap[0]

    if len(max_heap) > len(min_heap):
        return -max_heap[0]

    else:
        min_root = min_heap[0]
        max_root = -max_heap[0]
        return (min_root + max_root) / 2.0



def add(num, max_heap, min_heap):
    if len(min_heap) == 0 and len(max_heap) == 0:
        heapq.heappush(max_heap, -num)
        return

    median = get_median(max_heap, min_heap)

    if num > median:
        heapq.heappush(min_heap, num)
    else:
        heapq.heappush(max_heap, -num)

def rebalance(max_heap, min_heap):
    if len(max_heap) > (len(min_heap) + 1):
        root = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, root)
        
    if len(min_heap) > (len(max_heap) + 1):
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -root)

def print_median(max_heap, min_heap):
    print(get_median(max_heap, min_heap))


def running_median(stream):

    max_heap = []
    min_heap = []

    for num in stream:
        add(num,max_heap, min_heap)

        rebalance(max_heap, min_heap)

        print_median(max_heap, min_heap)



running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2    