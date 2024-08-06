import sys
sys.setrecursionlimit(100000)

def dfs(x, y, M, N, grid, visited):
    if x < 0 or x >= M or y < 0 or y >= N or grid[x][y] == '1' or visited[x][y]:
        return False
    if x == M - 1:  # 안쪽까지 도달하면
        return True
    
    visited[x][y] = True
    
    # 상하좌우 탐색
    return (dfs(x + 1, y, M, N, grid, visited) or
            dfs(x - 1, y, M, N, grid, visited) or
            dfs(x, y + 1, M, N, grid, visited) or
            dfs(x, y - 1, M, N, grid, visited))

def can_percolate(M, N, grid):
    visited = [[False] * N for _ in range(M)]
    
    # 바깥쪽 (위쪽 행)에서 전류를 흘려보내기 시작
    for j in range(N):
        if grid[0][j] == '0':  # 흰색 격자에서 시작
            if dfs(0, j, M, N, grid, visited):
                return "YES"
    return "NO"

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    
    M, N = map(int, data[0].split())
    grid = data[1:]
    
    result = can_percolate(M, N, grid)
    print(result)
