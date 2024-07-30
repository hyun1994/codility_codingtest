def solution(A):
    A = [1] + A + [1]
    checker = [0] * len(A)
    fibo = fibonacci(len(A))

    for i in range(1, len(A)):
        if A[i] == 0:
            continue
        min_cnt = len(A)

        for j in fibo[2:]:
            if i - j == 0 or (i - j >= 0 and checker[i - j] != 0):
                min_cnt = min(min_cnt, checker[i - j] + 1)

        if min_cnt != len(A):
            checker[i] = min_cnt

    if checker[-1] != 0:
        return checker[-1]
    else:
        return -1
    

def fibonacci(n):
    fibo = [0] * (n+2)
    fibo[1] = 1

    for i in range(2, n+2):
        fibo[i] = fibo[i-1] + fibo[i-2]

        if fibo[i] > n:
            return fibo[:i+1]
        
    return fibo