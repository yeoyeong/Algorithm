# 가로, 세로 이어저있는 풀때기를 하나로 침
# 각 풀의 좌표를 땐다
# FS(깊이 우선 탐색) 또는 BFS(너비 우선 탐색)를 사용
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

data = [input().strip() for _ in range(n)] 
#데이터를 좌표로 변환
matrix = [list(row) for row in data]


def dfs(x, y, grid, visited, n, m):
    #해당 좌표 체크 표시
    visited[x][y] = True
    
    #체크해야할 좌표
    directions = [(1, 0), (0, 1)]
    
    for dx, dy in directions:
        #현재 좌표에서 오른쪽, 아래 체크
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '#':
            dfs(nx, ny, grid, visited, n, m)


def count_grass_areas(grid, n, m):
    visited = [[False] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            # 해당 위치가 #이거나 visited 좌표가 false이면 실행
            if grid[i][j] == '#' and not visited[i][j]:
                dfs(i, j, grid, visited, n, m)
                count += 1
    
    return count




result = count_grass_areas(matrix, n, m)

print(result)

# list(row) 문자열 하나하나 스플릿