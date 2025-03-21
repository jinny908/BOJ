def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers)) # string 으로 바꿔야 문자열을 붙혀서 비교할 수 있다.
    numbers.sort(key = lambda x: x*3, reverse = True)
    
    for num in numbers:
        answer += num
        
    return str(int(answer))