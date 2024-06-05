def solution(X, A):
    cnt = 0
    visited = [0] * X
    
    for i in range(len(A)):
        if visited[A[i] - 1] == 0:
            visited[A[i] - 1] = 1
            cnt += 1
            if cnt == X:
                return i
    return -1