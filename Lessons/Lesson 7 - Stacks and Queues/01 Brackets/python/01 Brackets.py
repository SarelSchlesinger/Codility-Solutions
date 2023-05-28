def solution(S):
    
    stack = list()
    
    for i in S:
        if i in ['(','[','{']:
            stack.append(i)
        else:
            if len(stack) == 0:
                return 0
            top = stack.pop()
            if not ((top == '(' and i == ')') or (top == '{' and i == '}') or (top == '[' and i == ']')):
                return 0
    return 1 if len(stack) == 0 else 0