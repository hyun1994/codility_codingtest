def solution(S):
    stack = []

    for char in S:
        if not stack:
            stack.append(char)
        elif stack[-1] == "(" and char == ")":
            stack.pop()
        else:
            stack.append(char)

    if stack:
        return 0
    else:
        return 1