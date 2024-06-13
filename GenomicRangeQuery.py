def solution(S, P, Q):
    min_list = []

    for i in range(len(P)):
        DNA_1 = P[i]
        DNA_2 = Q[i]
        min_num = 5

        if 'A' in S[DNA_1:DNA_2+1]:
            num = 1
        elif 'C' in S[DNA_1:DNA_2+1]:
            num = 2
        elif 'G' in S[DNA_1:DNA_2+1]:
            num = 3
        elif 'T' in S[DNA_1:DNA_2+1]:
            num = 4

        if min_num > num:
            min_num = num
        min_list.append(min_num)

    return min_list