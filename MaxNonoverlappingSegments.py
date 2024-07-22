def solution(A, B):
    if not A:
        return 0
    
    endpoint = B[0]
    cnt = 1

    for idx, val in enumerate(A):
        if idx == 0:
            continue

        else:
            if val > endpoint:
                cnt = cnt + 1
                endpoint = B[idx]

    return cnt