def solution(A,B):
    stack = []
    cnt = 0

    for i in range(len(A)):
        if B[i] == 1:
            stack.append(A[i])
        else:
            if len(stack) == 0:
                cnt += 1
            else:
                if len(stack) == 0:
                    cnt += 1
                else:
                    for j in range(len(stack)-1, -1 , -1):
                        if stack[j] > A[i]:
                            break
                        else:
                            stack.pop(-1)
                    if len(stack) == 0:
                        cnt += 1
    return len(stack) + cnt