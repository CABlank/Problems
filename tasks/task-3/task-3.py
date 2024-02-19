def hIndex(publications):
    n = len(publications)
    citations = [0] * (n + 1)

    for publication in publications:
        if publication >= n:
            citations[n] += 1
        else:
            citations[publication] += 1

    
    total = 0
    i = n

    while i >= 0:
        total += citations[i]
        if total >= i:
            return i
        i -= 1
    return 0

print(hIndex([100, 5, 6, 6, 5]))