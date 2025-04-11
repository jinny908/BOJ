import sys
import heapq

from collections import deque

input = sys.stdin.readline

n, a, b = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_time = 0

for x in range(n):
    for y in range(n):
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        dist[x][y] = 0
        heap = [(0, x, y)]

        while heap:
            cost, x, y = heapq.heappop(heap)
            if dist[x][y] < cost:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] == grid[x][y]:
                        move_cost = a
                    else:
                        move_cost = b
                    if dist[nx][ny] > dist[x][y] + move_cost:
                        dist[nx][ny] = dist[x][y] + move_cost
                        heapq.heappush(heap, (dist[nx][ny], nx, ny))
        local_max = max(max(row) for row in dist)
        max_time = max(max_time, local_max)
print(max_time)


