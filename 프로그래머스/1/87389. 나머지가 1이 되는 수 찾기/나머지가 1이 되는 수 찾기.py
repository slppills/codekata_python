def solution(n):
    answer = 0
    if n % 2 != 0:
        return 2
    else:
        for i in range(3, n):
            if n % i == 1:
                return i