def solution(A, K):
    num - []
    if len(A) == 0:
        return A
    else :
        for i in range(K):
            num.append(A.pop())
            A.insert(0, num[i])
        return A