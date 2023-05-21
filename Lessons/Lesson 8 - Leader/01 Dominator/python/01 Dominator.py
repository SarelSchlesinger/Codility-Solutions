# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    if not A:
        return -1

    if len(A) == 1:
        return 0
        
    D = dict()
    for i in A:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1
    L = sorted(D.items(), key= lambda tup: tup[1], reverse= True)
    
    if not L[0][1] > len(A) * 0.5:
        return -1
    
    return A.index(L[0][0])