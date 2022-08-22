def solution(A):
    if not A:
        return 1
    return (len(A) + 1) * (len(A) + 2) // 2 - sum(A)