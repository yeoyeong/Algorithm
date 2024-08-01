# 가로, 세로 이어저있는 풀때기를 하나로 침
# 각 풀의 좌표를 땐다
# DFS(깊이 우선 탐색) 또는 BFS(너비 우선 탐색)를 사용
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

data = [input().strip() for _ in range(n)] 
#데이터를 좌표로 변환
matrix = [list(row) for row in data]

#dfs
def dfs(x, y, grid, visited, n, m):
    #해당 좌표 방문 체크
    visited[x][y] = True
    
    #"-" 체크해야할 좌표
    row_dx, row_dy = (0, 1)

    #"|" 체크해야할 좌표
    col_dx, col_dy = (1, 0)

    if grid[x][y]=="-":
        nx, ny = x + row_dx, y + row_dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == "-":
            dfs(nx, ny, grid, visited, n, m)

    if grid[x][y]=="|":
        nx, ny = x + col_dx, y + col_dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == "|":
            dfs(nx, ny, grid, visited, n, m)


def count_grass_areas(grid):
    visited = [[False] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            # 해당 위치가 #이거나 visited 좌표가 false이면 실행
            if not visited[i][j]:
                dfs(i, j, grid, visited, n, m)
                count += 1
    
    return count

result = count_grass_areas(matrix)

print(result)