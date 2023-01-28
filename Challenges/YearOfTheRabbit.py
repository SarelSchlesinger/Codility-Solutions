def solution(A, B):
    def solution1(A, B, numOfRotates = 0):
        if numOfRotates == len(A):
            return  - (1 + numOfRotates)
        for i in range(len(A)):
            if A[i] == B[i]:
                return 1 + solution1(A, [B[-1]] + B[:-1], numOfRotates + 1)
        return 0
    return solution1(A, B)