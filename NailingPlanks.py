BEGIN_POS = 0
END_POS = 1
NAIL_CNT_ADDRESS = 0
HIT_POS = 1


def solution(A, B, C):
    # Implement your solution here
    cnt = 0
    planks = zip(A, B)
    nails = sorted(enumerate(C), key = lambda var: var [HIT_POS])

    for plank in planks:
        nail_pos = binary_search(nails, plank)

        if nail_pos == -1:
            return -1

        nail_cnt = nails[nail_pos][NAIL_CNT_ADDRESS]

        while nail_pos < len(nails) and nails[nail_pos][HIT_POS] <= plank[END_POS]:
            nail_cnt = min(nail_cnt, nails[nail_pos][NAIL_CNT_ADDRESS])

            if nail_cnt <= cnt:
                break

            nail_pos += 1
        cnt = max(cnt, nail_cnt)

    return cnt + 1

def binary_search(nails, plank):
    beg = 0
    end = len(nails) - 1
    result = -1

    while beg <= end:
        mid = (beg + end) // 2

        if nails[mid][HIT_POS] < plank[BEGIN_POS]:
            beg = mid + 1
        elif nails[mid][HIT_POS] > plank[END_POS]:
            end = mid - 1
        else:
            end = mid - 1
            result = mid
    return result