def solution(A):
    east = 0
    num = 0
    max_num = 1000000000

    for i in range(len(A)):
        if A[i] == 0 :
            east += 1
        else:
            num += east

    if num > max_num:
        return -1
    
    return num