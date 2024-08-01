#내코드x
import sys

input = sys.stdin.readline
n = int(input().strip())

data = [input().strip() for _ in range(n)]

# 데이터를 좌표로 변환
matrix = [list(map(int, row.split())) for row in data]

WIN_MESSAGE = "HaruHaru"
LOSE_MESSAGE = "Hing"

# DFS를 반복문으로 구현
def iterative_dfs(start_x, start_y, grid, n):
    stack = [(start_x, start_y)]
    visited = set()

    while stack:
        x, y = stack.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if grid[x][y] == -1:
            return True

        move = grid[x][y]
        directions = [(move, 0), (0, move)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                stack.append((nx, ny))

    return False

# 게임 결과 확인
def count_grass_areas(grid):
    if iterative_dfs(0, 0, grid, n):
        return WIN_MESSAGE
    else:
        return LOSE_MESSAGE

result = count_grass_areas(matrix)
print(result)