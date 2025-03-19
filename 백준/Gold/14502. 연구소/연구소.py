import sys
from collections import deque
from itertools import combinations  # ✅ 추가
import copy

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# bfs로 바이러스 퍼지는 과정
def bfs():
    queue = deque()
    tmp_graph = [row[:] for row in graph]  # ✅ 얕은 복사로 tmp_graph 만들기
    dx = [-1, 1, 0, 0]  # 상 하
    dy = [0, 0, -1, 1]  # 좌 우

    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if tmp_graph[nx][ny] == 0:  # 감염 가능한지 체크
                    tmp_graph[nx][ny] = 2  # 감염
                    queue.append((nx, ny))

    global answer
    cnt = 0
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    answer = max(answer, cnt)

# ✅ 빈칸 위치만 뽑기
empty = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]

# ✅ 조합으로 벽 3개를 세우고 BFS 수행
answer = 0
for walls in combinations(empty, 3):
    # 벽 세우기
    for x, y in walls:
        graph[x][y] = 1

    bfs()

    # 벽 허물기
    for x, y in walls:
        graph[x][y] = 0

print(answer)
