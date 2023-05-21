def solution(A):
    if len(A) == 1:
        return A[0]
    d = {}
    for i in A:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for key in d:
        if d.get(key) % 2 == 1:
            return key