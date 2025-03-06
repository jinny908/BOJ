from collections import deque

def is_edge_connected(x, y, n, m, grid):
    if x == 0 or x == n-1 or y == 0 or y == m-1:
        return True
    visited = set()
    queue = deque()
    queue.append((x, y))
    visited.add((x, y))
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] is None and (nx, ny) not in visited:
                    if nx == 0 or nx == n-1 or ny == 0 or ny == m-1:
                        return True
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return False

def is_accessible(i, j, n, m, grid):
    if i == 0 or i == n-1 or j == 0 or j == m-1:
        return True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        ni = i + dx
        nj = j + dy
        if 0 <= ni < n and 0 <= nj < m:
            if grid[ni][nj] is None:
                if is_edge_connected(ni, nj, n, m, grid):
                    return True
    return False

def solution(storage, requests):
    if not storage:
        return 0
    n = len(storage)
    m = len(storage[0])
    grid = [list(s) for s in storage]
    
    for req in requests:
        if len(req) >= 2 and all(c == req[0] for c in req):
            target = req[0]
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == target:
                        grid[i][j] = None
        else:
            if not req:
                continue
            target = req[0]
            remove_list = []
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == target:
                        if is_accessible(i, j, n, m, grid):
                            remove_list.append((i, j))
            for i, j in remove_list:
                grid[i][j] = None
    count = 0
    for row in grid:
        for cell in row:
            if cell is not None:
                count += 1
    return count