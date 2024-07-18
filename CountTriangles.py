def solution(A):
    A = sorted(A)
    result = 0

    for p in range(len(A)):
        r = p + 2

        for q in range(p+1, len(A)):
            while r < len(A) and A[p] + A[q] > A[r]:
                r += 1

            result += r - q - 1

    return result