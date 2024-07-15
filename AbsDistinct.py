def solution(A):
    set_a = set()

    for i in range(len(A)):
        a_abs = abs(A[i])
        set_a.add(a_abs)

    return len(set_a)