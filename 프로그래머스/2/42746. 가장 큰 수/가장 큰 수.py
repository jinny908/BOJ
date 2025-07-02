def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers)) # string으로 변경하기
    numbers.sort(key=lambda x:x*3, reverse = True)
    answer = ''.join(numbers)
    return str(int(answer))