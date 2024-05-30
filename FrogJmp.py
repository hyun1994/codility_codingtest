def solution(X, Y, D):
    cnt = 0
    dist = Y - X
    if dist % D == 0:
        cnt = dist//D
        return cnt
    else:
        cnt = dist//D + 1
        return cnt