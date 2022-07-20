def solution(A, K):
    if not A:
        return A
    while K > 0:
        A = [A[-1]] + A[:-1]
        K -= 1
    return A