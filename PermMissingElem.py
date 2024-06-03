def solution(A):
    A = sorted(A)
    N = len(A) + 1
    num = 0
    for i in range(1, N+1):
        num += i
    
    Anum = 0
    for i in A:
        Anum += i
    
    result = num - Anum
    return result