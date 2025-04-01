import sys
from collections import deque
from zipfile import error

input = sys.stdin.readline

t = int(input())
for i in range(t):
    cmd = list(input().strip())
    n = int(input())
    arr = input().strip()

    if arr == "[]":
        queue = deque()
    else:
        queue = deque(arr[1:-1].split(','))

    reversed = False
    error_flag = False

    for c in cmd:
        if c == 'R':
            reversed = not reversed
        elif c == 'D':
            if not queue:
                error_flag = True
                break
            if reversed:
                queue.pop()
            else:
                queue.popleft()
        
    if error_flag:
        print('error')
    else:
        if reversed:
            queue.reverse()
        print('[' + ','.join(queue) + ']')

