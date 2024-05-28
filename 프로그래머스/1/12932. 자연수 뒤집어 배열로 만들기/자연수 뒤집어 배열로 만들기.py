def solution(n):
    n = list(str(n))
    answer = []
    for i in n:
        answer.append(int(i))
    answer.reverse()
    return answer