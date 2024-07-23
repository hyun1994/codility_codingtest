def solution(K, A):
    cnt = 0
    rope_A = 0

    for i in A:
        rope_A += i
        if rope_A >= K:
            cnt += 1
            rope_A = 0

    return cnt