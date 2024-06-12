def solution(A, B, K):
    div_A = A // K
    div_B = B // K
    cnt = 0

    if A % K == 0:
        cnt += 1
        return div_B - div_A + cnt
    else:
        cnt = 0
        return div_B - div_A + cnt