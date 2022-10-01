def solution(N):
    newN = str(bin(N))[2:]
    newN = newN.strip('0')
    L = newN.split('1')
    return len(max(L))