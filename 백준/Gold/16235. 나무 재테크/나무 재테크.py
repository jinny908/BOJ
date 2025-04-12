import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int,input().split())
feed = [list(map(int, input().split())) for _ in range(n)]
tree = [list(map(int, input().split())) for _ in range(m)] # [x, y, age]
land = [[5]*n for _ in range(n)]
tree_map = [[deque() for _ in range(n)] for _ in range(n)]
dead = [[[] for _ in range(n)] for _ in range(n)]

for x, y, age in tree:
    tree_map[x-1][y-1].append(age)

for i in range(n):
    for j in range(n):
        tree_map[i][j] = deque(sorted(tree_map[i][j]))
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def spring_summer():
    for i in range(n):
        for j in range(n):
            alive = deque()
            for _ in range(len(tree_map[i][j])):
                age = tree_map[i][j].popleft()
                if land[i][j] >= age:
                    land[i][j] -= age
                    alive.append(age + 1)
                else:
                    dead[i][j].append(age)
            tree_map[i][j] = alive

    for i in range(n):
        for j in range(n):
            for age in dead[i][j]:
                land[i][j] += age // 2
            dead[i][j].clear() # 다음 년도를 위해 초기화

def fall_winter():
    for i in range(n):
        for j in range(n):
            for age in tree_map[i][j]:
                if age % 5 == 0:
                    for dir in range(8):
                        nx = i + dx[dir]
                        ny = j + dy[dir]
                        if 0 <= nx < n and 0 <= ny < n:
                            tree_map[nx][ny].appendleft(1)
            land[i][j] += feed[i][j]


for year in range(k):
    spring_summer()
    fall_winter()

result = 0
for i in range(n):
    for j in range(n):
        result += len(tree_map[i][j])
print(result)
