def solution(n):
    answer = ''
    arr = list(str(n))
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if int(arr[i]) < int(arr[j]):
                arr[i], arr[j] = arr[j], arr[i] # swap(두 값을 변환)
        answer += arr[i]
    answer += arr[len(arr)-1]
    return int(answer)