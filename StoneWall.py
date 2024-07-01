def solution(H):
    cnt = 0
    stack = []

    for i in range(len(H)):
        while len(stack) > 0 and stack[-1] > H[i]:
            stack.pop()

        if len(stack) == 0 or stack[-1] < H[i]:
            cnt += 1
            stack.append(H[i])

    return cnt