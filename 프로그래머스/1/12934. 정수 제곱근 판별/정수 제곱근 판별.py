def solution(n):
    a = n ** (1/2) # 소숫점 붙어서 나옴
    if a == int(a): # n이 121일 때 a의 값인 11.0과 a를 정수형으로 바꾼 11이 같은지 비교
        return (a+1) ** 2
    else:
        return -1
