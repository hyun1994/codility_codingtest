def solution(N):
    # Implement your solution here
    tmp = []
    cnt = 0
    cnt_max = 0

    while True:
        num = N % 2
        N = N // 2
        tmp.append(num)

        if N < 2:
            tmp.append(N)
            break
    tmp.reverse()

    for t in tmp:
        if t == 1 :
            if cnt_max < cnt :
                cnt_max = cnt
            cnt = 0
        else :
            cnt += 1
    if tmp.count(1) == 1:
        cnt_max = 0
    return cnt_max