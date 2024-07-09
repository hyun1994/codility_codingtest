def solution(N):
    num = 0

    for i in range(1, N+1):
        if i*i > N:
            break

        if i*i == N:
            num += 1
            break

        if N % i == 0:
            num += 2

    return num