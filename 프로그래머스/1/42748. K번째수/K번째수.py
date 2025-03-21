def solution(array, commands):
    arr = []
    answer = []
    for cmd in commands:
        arr = sorted(array[cmd[0]-1:cmd[1]])
        answer.append(arr[cmd[2]-1])
    
    return answer