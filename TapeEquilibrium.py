def solution(A):
    dist = []
    dist_a = 0
    A_sum = sum(A)
    for i in range(len(A)-1):
        dist_a += A[i]
        dist_b = A_sum - dist_a
        dist.append(abs(dist_a - dist_b))
    return min(dist)