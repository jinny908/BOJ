import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    cnt = 0
    
    while queue:
        top = max(queue)
        pop = queue.popleft()
        m -= 1

        if top == pop:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            queue.append(pop)
            if m < 0:
                m = len(queue) - 1

