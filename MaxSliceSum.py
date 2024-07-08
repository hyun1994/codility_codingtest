def solution(A):
    maxsum = -float('inf')
    asum = 0

    for a in A:
        asum += a
        maxsum = max(maxsum, asum)
        asum = max(0, asum)

    return maxsum