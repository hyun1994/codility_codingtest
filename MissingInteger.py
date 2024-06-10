def solution(A):
    A = sorted(A)
    A = list(set(A))
    cnt = 1

    for a in A:
        if a == cnt:
            cnt += 1
    return cnt