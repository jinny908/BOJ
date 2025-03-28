import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
position = list(map(int, input().split()))
queue = deque(i for i in range(1,n+1))
cnt = 0

for i in position:
    idx = queue.index(i) # idx = 0 based index 임
    if idx <= len(queue) // 2:
        queue.rotate(-idx)
        cnt += idx
    else:
        queue.rotate(len(queue) - idx)
        cnt += len(queue) - idx
    queue.popleft()
print(cnt)