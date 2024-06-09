import collections
def solution(N, A):
    # Implement your solution here
    max_cnt = 0
    A_left = -1
    A_right = -1

    for i, n in enumerate(A):
        if n > N:
            A_left, A_right = A_right+1, i
            if A[A_left:A_right]:
                increase = collections.Counter(A[A_left:A_right])
                max_cnt += max(increase.values())

    if len(A) == A_right:
        return [max_cnt] * N
    else:
        cnt = [max_cnt] * N
        increase = collections.Counter(A[A_right+1:])
        for key, val in increase.items():
            cnt[key-1] += val
        return cnt