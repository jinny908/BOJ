import sys

input = sys.stdin.readline

graph = [
    [1], [2], [3], [4], [5],
    [6, 21], [7], [8], [9], [10],
    [11, 25], [12], [13], [14], [15],
    [16, 27], [17], [18], [19], [20],
    [32],     # 20 -> 도착(32)
    [22], [23], [24], [30],   # 21~24: 분기 경로(13 → 25)
    [26], [24],               # 25, 26: 분기 경로(22 → 25)
    [28], [29], [24],         # 27~29: 분기 경로(28 → 25)
    [31], [20], [32]          # 30, 31: 30→35→40 / 32 = 도착
]

# 칸별 점수
score = [
    0, 2, 4, 6, 8,
    10, 12, 14, 16, 18,
    20, 22, 24, 26, 28,
    30, 32, 34, 36, 38,
    40, 13, 16, 19, 25,
    22, 24, 28, 27, 26,
    30, 35, 0
]

dice = list(map(int, input().split()))
position = [0] * 4
used = [False] * 33 # 전체 칸 점유 여부 (도착 칸 예외)
answer = 0

def move(pos, dice_val): # 분기점에서 경로 선택하는 함수
    first = True
    for _ in range(dice_val):
        if pos == 32:
            return 32
        if first and len(graph[pos]) == 2:
            pos = graph[pos][1]
        else:
            pos = graph[pos][0]
        first = False
    return pos

def dfs(turn, total):
    global answer
    if turn == 10:
        answer = max(total, answer)
        return
    for i in range(4):
        now = position[i]
        if now == 32:
            continue
        new_pos = move(now, dice[turn])
        if new_pos != 32 and used[new_pos]:
            continue

        before_pos = position[i]
        position[i] = new_pos
        if new_pos != 32:
            used[new_pos] = True
        if before_pos != 32:
            used[before_pos] = False

        # 다음턴
        dfs(turn + 1, total + score[new_pos])

        # 백트래킹 복구
        position[i] = before_pos
        if new_pos != 32:
            used[new_pos] = False
        if before_pos != 32:
            used[before_pos] = True

dfs(0,0)
print(answer)