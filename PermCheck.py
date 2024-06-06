def solution(A):
    # Implement your solution here
    A = sorted(A)
    cnt = 1

    for a in A:
        if a == cnt:
            cnt += 1
        else:
            return 0
    return 1