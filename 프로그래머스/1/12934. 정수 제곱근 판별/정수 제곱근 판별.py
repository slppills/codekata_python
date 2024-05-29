def solution(n):
    a = n ** (1/2) # 소숫점 붙어서 나옴
    if a == int(a):
        return (a+1) ** 2
    else:
        return -1