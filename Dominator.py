def solution(A):
    cnt = 0
    max_cnt = 0
    dict = {}

    if not A:
        return -1
    
    for a in A:
        if not a in dict:
            dict[a] = 1
        else:
            dict[a] += 1
        
        if dict[a] > cnt:
            max_cnt = a
            cnt = dict[a]

    if cnt > int(len(A)/2):
        return A.index(max_cnt)
    else:
        return -1