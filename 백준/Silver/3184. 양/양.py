from collections import deque

def bfs(x, y, R, C, yard, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    sheep = 0
    wolf = 0
    
    if yard[x][y] == 'o':
        sheep += 1
    elif yard[x][y] == 'v':
        wolf += 1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and yard[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))
                if yard[nx][ny] == 'o':
                    sheep += 1
                elif yard[nx][ny] == 'v':
                    wolf += 1
    
    # 영역 내에서 양과 늑대의 수를 비교
    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf

def count_survivors(R, C, yard):
    visited = [[False] * C for _ in range(R)]
    total_sheep = 0
    total_wolves = 0
    
    for i in range(R):
        for j in range(C):
            if not visited[i][j] and yard[i][j] != '#':
                sheep, wolf = bfs(i, j, R, C, yard, visited)
                total_sheep += sheep
                total_wolves += wolf
    
    return total_sheep, total_wolves

if __name__ == "__main__":
    R, C = map(int, input().split())
    yard = [list(input().strip()) for _ in range(R)]
    
    result_sheep, result_wolves = count_survivors(R, C, yard)
    print(result_sheep, result_wolves)
