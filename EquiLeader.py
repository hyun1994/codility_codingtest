import collections
def solution(A):
    a_len = len(A)
    a_dict = collections.defaultdict(int)
    a_num = 0

    for i, num in enumerate(A):
        a_dict[num] += 1

        if a_dict[num] > a_len / 2:
            a_num = num

    result = 0
    cnt = 0

    for i, num in enumerate(A):
        if num == a_num:
            cnt += 1
        if cnt > (i+1) / 2 and a_dict[num] - cnt > (a_len - i - 1) / 2:
            result += 1

    return result