def solution(T):
    d = dict()
    for tower in T:
        if tower not in d:
            d[tower] = 1
        else:
            d[tower] += 1
        if tower[0]+tower[2]+tower[1] != tower:
            if tower[0]+tower[2]+tower[1] not in d:
                d[tower[0]+tower[2]+tower[1]] = 1
            else:
                d[tower[0]+tower[2]+tower[1]] += 1
        if tower[1]+tower[0]+tower[2] != tower:
            if tower[1]+tower[0]+tower[2] not in d:
                d[tower[1]+tower[0]+tower[2]] = 1
            else:
                d[tower[1]+tower[0]+tower[2]] += 1     
    return max(d.values())