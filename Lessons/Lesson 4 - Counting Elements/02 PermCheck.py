# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort(reverse=True)
    for index, value in enumerate(A):
        if value != len(A) - index:
            return 0
    return 1

