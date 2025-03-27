import sys

input = sys.stdin.readline

n, k = map(int,input().split())
chess_map = [list(map(int,input().split())) for _ in range(n)]
# 각 칸에 쌓여 있는 말들의 번호 저장 (맨 아래는 0)
curr_map = [[[] for _ in range(n)] for _ in range(n)]
# 각 말의 정보: [행,열,방향]
chess = [None for _ in range(k)]

for i in range(k):
    x, y, d = map(int,input().split())
    curr_map[x-1][y-1].append(i)
    chess[i] = [x-1, y-1, d-1]

# 방향 정의 (1 오른쪽 2 왼쪽 3 위 4 아래)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def reverse_dir(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

turn = 0
finish = False

while turn <= 1000 and not finish:
    turn += 1
    for i in range(k):
        x, y, d = chess[i]
        if not curr_map[x][y] or curr_map[x][y][0] != i: # 맨 아래 칸 말이 차례가 아니라면 건너뛰기
            continue
        idx = curr_map[x][y].index(i)
        moving_stack = curr_map[x][y][idx:] # 이동하는 말
        curr_map[x][y] = curr_map[x][y][:idx] # 남은 말

        # 1. 이동하려는 칸 계산
        nx = x + dx[d]
        ny = y + dy[d]

        # 2. 먼저 파란색 또는 범위 밖인지 확인
        if not (0 <= nx < n and 0 <= ny < n) or chess_map[nx][ny] == 2:
            # 방향 바꾸고 재시도
            nd = reverse_dir(d)
            chess[i][2] = nd
            nx = x + dx[nd]
            ny = y + dy[nd]

            # 재시도한 칸도 안 되면 이동 안 함
            if not (0 <= nx < n and 0 <= ny < n) or chess_map[nx][ny] == 2:
                curr_map[x][y].extend(moving_stack)  # 원래 위치에 다시 쌓기
                continue
            else:
                d = nd  # 새로운 방향 유지

        # 3. 이제 정상적인 칸이면 색상에 따라 이동 처리
        if chess_map[nx][ny] == 0:  # white
            curr_map[nx][ny].extend(moving_stack)
        elif chess_map[nx][ny] == 1:  # red
            moving_stack.reverse()
            curr_map[nx][ny].extend(moving_stack)

        for horse in moving_stack: # 이동한 말들 위치 갱신
            chess[horse][0] = nx
            chess[horse][1] = ny

        if len(curr_map[nx][ny]) >= 4:
            finish = True
            break
    if finish:
        break

print(-1 if turn > 1000 else turn)