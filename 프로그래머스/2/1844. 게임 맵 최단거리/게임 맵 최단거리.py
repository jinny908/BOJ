from collections import deque

def solution(maps):
    answer = 0
    r, c = len(maps), len(maps[0])
    # 상하좌우
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny)) # 재귀
        
        return maps[r-1][c-1]
    
    answer = bfs(0,0)
    if answer == 1:
        return -1
    else:
        return answer
    







