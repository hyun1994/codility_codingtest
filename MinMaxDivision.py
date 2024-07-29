def valid(A, K, max_sum):
    block_sum = 0
    block_cnt = 0

    for a in A:
        block_sum += a
        if block_sum > max_sum:
            block_sum = a
            block_cnt += 1

    return block_cnt + 1 <= K

def solution(K, M, A):
    min_val = max(A)
    max_val = sum(A)

    while min_val <= max_val:
        mid = (min_val + max_val) // 2

        if valid(A, K, mid):
            max_val = mid - 1
        else:
            min_val = mid + 1

    return min_val