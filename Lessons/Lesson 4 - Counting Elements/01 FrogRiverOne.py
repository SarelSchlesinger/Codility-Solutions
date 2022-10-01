# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    
    if X > len(A):
        return -1
    
    if X == 1:
        return A.index(1)
    
    d = {}
    
    for index, value in enumerate(A):
        if value > X:
            continue
        elif value not in d:
            d[value] = index
        if len(d) == X:
            return max(d.values())
    
    return -1