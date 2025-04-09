import sys

from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0] * 100001

def bfs(now):
    queue = deque()
    queue.append(now)

    while queue:
        now = queue.popleft()
        if now == k:
            return visited[now]
        for i in (now + 1, now -1, 2 * now):
            if 0 <= i < len(visited) and visited[i] == 0:
                visited[i] = visited[now] + 1
                queue.append(i)
print(bfs(n))