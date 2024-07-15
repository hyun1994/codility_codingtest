def solution(N, M):
    a, b = N, M

    while(b):
        a, b = b, a % b

    gcd = a
    result = N // gcd

    return result