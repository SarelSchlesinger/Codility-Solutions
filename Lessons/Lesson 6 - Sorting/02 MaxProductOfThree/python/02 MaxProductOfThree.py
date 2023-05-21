def solution(A):
    A = sorted(A, reverse=True)
    return max(A[0] * A[1] * A[2], A[-1] * A[-2] * A[0])