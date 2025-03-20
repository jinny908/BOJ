def solution(grid):
    n, m = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    
    # 상우하좌 시계방향
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    def turn(d, cmd):
        if cmd == 'L':
            return (d + 3) % 4
        elif cmd == 'R':
            return (d + 1) % 4
        else:
            return d
                    
    answer = []
    
    for x in range(n):
        for y in range(m):
            for d in range(4):
                if not visited[x][y][d]:
                    cnt = 0
                    nx, ny, nd = x, y, d
                    
                    while not visited[nx][ny][nd]:
                        visited[nx][ny][nd] = True
                        cnt += 1
                        
                        nx = (nx + dx[nd]) % n
                        ny = (ny + dy[nd]) % m
                        
                        nd = turn(nd, grid[nx][ny])
                        
                    if cnt > 0:
                        answer.append(cnt)
    return sorted(answer)
