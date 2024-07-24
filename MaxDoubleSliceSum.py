def solution(A):
    n = len(A)
    x = [0] * n
    z = [0] * n

    for i in range(1, n-1):
        x[i] = max(0, x[i-1]+A[i])
    for i in range(n-1, 0, -1):
        z[i-1] = max(0, z[i]+A[i-1])

    result = 0

    for i in range(1, n-1):
        result = max(result, x[i-1]+z[i+1])

    return result