import math
def solution(N):
    num = int(math.sqrt(N))
    div = 1

    for i in range(1, num+1):
        if N % i == 0:
            div = i

    return 2*(div + int(N/div))