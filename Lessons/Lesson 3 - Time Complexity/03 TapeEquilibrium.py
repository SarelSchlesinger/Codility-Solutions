def solution(A):
    left = A[0]
    right = sum(A[1:])
    res = abs(left - right)
    for i in range(1, len(A) - 1):
        left += A[i]
        right -= A[i]
        if abs(left - right) < res:
            res = abs(left - right)
    return res