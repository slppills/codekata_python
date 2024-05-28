def solution(n):
    answer = 0
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            answer += i
            if i < n**(1/2):
                answer += n / i
    return answer