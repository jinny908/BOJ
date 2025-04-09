import sys

from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
# 보통 나오는 n 은 세로, m 은 가로인데 이 문제는 반대로 되어 헷갈린다.

tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)]for _ in range(h)]

# 6방향 전개를 어떻게 구현할까 ... ?
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()

# m = x, n = y, h = z

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if tomato[nz][nx][ny] == 0 and not visited[nz][nx][ny]:
                    tomato[nz][nx][ny] = tomato[z][x][y] + 1
                    visited[nz][nx][ny] = True
                    queue.append((nz, nx, ny))

def solution():
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if tomato[z][x][y] == 1:
                    queue.append((z, x, y))
                    visited[z][x][y] = True

    bfs()

    answer = 0
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if tomato[z][x][y] == 0:
                    return -1
                answer = max(answer, tomato[z][x][y])
    return answer -1
print(solution())
