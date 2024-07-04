def solution(A):
    if len(A) < 2:
        return 0
    
    maxprofit = 0
    val = A[0]

    for i in range(1, len(A)):
        if val > A[i]:
            val = A[i]
        profit = A[i] - val
        if profit > maxprofit:
            maxprofit = profit
    return maxprofit