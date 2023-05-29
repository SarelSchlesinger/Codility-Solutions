def solution(A):
    flag = False
    res = 0
    inc = 1
    for i in A:
        if i == 0:
            if flag == False:
                flag = True
            else:
                inc += 1
        else:
            if flag == True:
                res += inc
    return res if res <= 1e9 else -1