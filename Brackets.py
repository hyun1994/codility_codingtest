def solution(S):
    table = {"(":")", "{":"}","[":"]"}
    stack = []

    for char in S:
        if table.get(char, False):
            stack.append(char)
        else:
            if not stack or table[stack.pop()] != char:
                return 0
    
    if stack:
        return 0
    else:
        return 1