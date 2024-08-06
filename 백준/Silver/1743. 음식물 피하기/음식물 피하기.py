import sys
from collections import deque

def bfs(start, grid, visited, N, M):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    size = 1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1
    
    return size

def find_largest_trash(N, M, K, trash_locations):
    grid = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    for r, c in trash_locations:
        grid[r - 1][c - 1] = 1  # 좌표를 격자에 반영 (1-based index -> 0-based index)
    
    max_size = 0
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                size = bfs((i, j), grid, visited, N, M)
                max_size = max(max_size, size)
    
    return max_size

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    
    N, M, K = map(int, data[0].split())
    trash_locations = [tuple(map(int, line.split())) for line in data[1:]]
    
    result = find_largest_trash(N, M, K, trash_locations)
    print(result)
